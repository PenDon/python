"""
WordCloud of Reviews of FengXinLou
Created By Peng 2021/10/26
"""
import pandas as pd
import jieba.posseg as psg
import pyecharts.options as opts
from pyecharts.charts import WordCloud

df = pd.io.json.read_json('data.json')
df['pub_date'] = pd.to_datetime(df['pub_date'], unit='s')

# todo 时间维度分析
# df_date = pd.DataFrame(index=df['pub_date'], data=[1] * df['pub_date'].size, columns=['count'])
# df_new = df_date.resample('1d').sum()

word_list = df['content'].to_list()
words = "\n".join(word_list)

res = {}
stop_words = ['没有', '感觉', '希望', '不能', '觉得', '有点', '时候', '时间', '小时', '可能', '增加', '还有', '知道', '不同', '只能', '直接', '问题',
              '东西', '普通', '容易', '无法', '大量', '目的', '', '', '']

roles_list = ['王爷', '容都王', '师爷', '一一', '双双', '栗子', '聂香', '香香', '夕芸', '咕咕', '鸽子', '吴氏', '雎鸠', '玉漏', '仙子']
for word in psg.cut(words):
    # if word.word in stop_words:
    #     continue
    # if len(word.word) == 1:
    #     continue
    # # 过滤非名词形容词
    # if word.flag.startswith('n') or word.flag.startswith('a'):
    #     pass
    # else:
    #     continue
    if word.word in roles_list:
        pass
    else:
        continue
    if word.word in res:
        res[word.word] += 1
    else:
        res[word.word] = 1

data_word_list = sorted(res.items(), key=lambda x: x[1], reverse=True)

chart = WordCloud(init_opts=opts.InitOpts(width='1200px', height='900px'))\
    .add(series_name="Reviews", data_pair=data_word_list, word_size_range=[10, 80])\
    .set_global_opts(title_opts=opts.TitleOpts(title="xxxx", title_textstyle_opts=opts.TextStyleOpts(font_size=36)),
                     tooltip_opts=opts.TooltipOpts(is_show=True), )
chart.render('Roles.html')
