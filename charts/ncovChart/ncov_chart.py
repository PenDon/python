from pyecharts.charts import Timeline, Bar
import pyecharts.options as opts
import pandas as pd
import tushare as ts
from pyecharts.globals import ThemeType


def get_chart(title: str, current: dict) -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1800px", height="800px")).add_xaxis(list(current.keys()))
        .add_yaxis("数据", list(current.values()))
            .set_global_opts(title_opts=opts.TitleOpts(title="统计", subtitle="副标题"),
                             xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-25, font_size=16)), )
    )
    return bar


timeline = Timeline(init_opts=opts.InitOpts(width="1600px", height="800px"))

pro = ts.pro_api("af279b19570943e00c2de22f5812f7356c8a07da1296f0e721fbeabc")

df = pro.ncov_num(level=3, fields=['ann_date', 'area_name', 'confirmed_num'])
df = df[df['area_name'] != '湖北省']
dates = list(df['ann_date'].unique())

for date in dates:
    if not date:
        continue
    timeline.add(get_chart(title=date, current=df[df['ann_date'] == date].sort_values(by='confirmed_num').tail(10)
    [['area_name', 'confirmed_num']].set_index('area_name').to_dict()['confirmed_num']), time_point=date)

timeline.add_schema(is_auto_play=True, play_interval=1000)
timeline.render("advanced.html")
