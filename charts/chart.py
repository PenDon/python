from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType
from myLib.mysql import Mysql
import pandas as pd

mysql = Mysql(dbName="mlyj_ad_cost", debug=False)
result = mysql.execute_sql(
    'SELECT SUM(ac.amount) as s, ac.month, a.member_name FROM ad_cost ac LEFT JOIN account a ON ac.account_name = a.account_name WHERE ac.amount <> 0 GROUP BY a.member_name, ac.month ')

df = pd.DataFrame(data=result)
df[0] = round(df[0], 2)

# print(df[2].drop_duplicates().values.tolist())
xaxis = df[2].drop_duplicates().values.tolist()
print(xaxis)

y1axis = df[df[1] == '4']
y1axis = y1axis[0].tolist()

y2axis = df[df[1] == '5']
y2axis = y2axis[0].tolist()

y3axis = df[df[1] == '6']
y3axis = y3axis[0].tolist()

# bar = (
#     Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#     .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
#     .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
# )

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1800px", height="900px"))
    .add_xaxis(xaxis)
    .add_yaxis("4月", y1axis)
    .add_yaxis("5月", y2axis)
    .add_yaxis("6月", y3axis)
    .set_global_opts(title_opts=opts.TitleOpts(title="广告金额统计", subtitle="副标题"), xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-25, font_size=16)),)
)
bar.render()