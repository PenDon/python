import pyecharts.options as opts
from pyecharts.charts import Timeline, Bar
from myLib.mysql import Mysql
import pandas as pd
from pyecharts.globals import ThemeType


def get_chart(title: str, current: pd.DataFrame) -> Bar:
    # 每月的数据
    y1axis = current[current[1] == '4'][0].tolist()
    y2axis = current[current[1] == '5'][0].tolist()
    y3axis = current[current[1] == '6'][0].tolist()
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1800px", height="800px"))
            .add_xaxis([title])
            .add_yaxis("4月", y1axis if y1axis else [0])
            .add_yaxis("5月", y2axis if y2axis else [0])
            .add_yaxis("6月", y3axis if y3axis else [0])
            .set_global_opts(title_opts=opts.TitleOpts(title="广告金额统计", subtitle="副标题"),
                             xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-25, font_size=16)), )
    )
    return bar


timeline = Timeline(init_opts=opts.InitOpts(width="1600px", height="800px"))

mysql = Mysql(dbName="mlyj_ad_cost", debug=False)
result = mysql.execute_sql(
    'SELECT SUM(ac.amount) as s, ac.month, a.member_name FROM ad_cost ac LEFT JOIN account a ON ac.account_name = a.account_name WHERE ac.amount <> 0 GROUP BY a.member_name, ac.month ')

df = pd.DataFrame(data=result)
df[0] = round(df[0], 2)

names = df[2].drop_duplicates().values.tolist()

for name in names:
    if not name:
        continue
    timeline.add(get_chart(title=name, current=df[df[2] == name]), time_point=name)

timeline.add_schema(is_auto_play=True, play_interval=2000)
timeline.render("advanced.html")
