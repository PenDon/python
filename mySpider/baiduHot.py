import requests
from lxml import etree
from myLib.header import get_header

res = requests.get("https://www.baidu.com", headers=get_header()).text
tree = etree.HTML(res)

# 部分热搜
lis = tree.xpath('//*[@class="s-hotsearch-content"]/li')
for li in lis:
    print(li.xpath('./a/span/text()'))

# 全部热搜 - json格式
json = tree.xpath('//*[@id="hotsearch_data"]/text()')[0]
print(json)
