import requests
from lxml import etree
import json

# 必须加 referer, 否则第一次请求无结果
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/74.0.3729.157 Safari/537.36',
    'referer': "https://mall.jd.com/"
}

info = requests.get(
    'https://module-jshop.jd.com/module/getModuleHtml.html?orderBy=99&direction=1&pageNo=1&categoryId=9061630'
    '&pageSize=20&pagePrototypeId=8&pageInstanceId=111774908&moduleInstanceId=258367169&prototypeId=55555&templateId'
    '=905542&appId=1056224&layoutInstanceId=258367169&origin=0&shopId=813953&venderId=815911&callback'
    '=jshop_module_render_callback', headers=headers).text
info = info[29:-1]

json_info = json.loads(info)

# 抓取商品SKU
tree = etree.HTML(json_info['moduleText'])
skus = tree.xpath('//span[@class="jdNum"]/@jdprice')

# 商品SKU前加上  J_
new_skus = ['J_' + sku for sku in skus]

# 使用多个商品SKU 请求价格接口
skus_string = ','.join(new_skus)
result = requests.get(f'https://f-mall.jd.com/prices/mgets?source=jshop&type=mgets&area=18_1482_48939_0&skuids={skus_string}&_=1624516262221', headers=headers).json()
print(result)

# result: 结果是一个json，包含所有请求商品的价格
# [{'p': '69.00', 'op': '69.00', 'm': '169.00', 'cbf': 0, 'id': 'J_69200853812'}, {'p': '179.00',
# 'op': '179.00', 'm': '369.00', 'cbf': 0, 'id': 'J_66266801909'}, ... 省略
