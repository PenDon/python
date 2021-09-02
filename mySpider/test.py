import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/74.0.3729.157 Safari/537.36',
}

res = requests.get('https://www.leleketang.com/let3/my_ppts.php', headers=headers)
tree = etree.HTML(res.text)

menu = tree.xpath('//*[@id="catalog_root"]/div')
menu_list = []
for item in menu:
    links = item.xpath('.//a')
    for link in links:
        item_name = link.xpath('./@data-name')[0]
        item_depth = link.xpath('./@data-step')[0]
        item_href = link.xpath('./@href')

        menu_list.append({"name": item_name, "depth": item_depth, "href": item_href[0] if item_href else ''})

print(menu_list)
# Result: [{'name': '人教版七年级下', 'depth': '0', 'href': 'javascript:;'}, {'name': '相交线与平行线', 'depth': '1', 'href': 'javascript:;'}, {'name': '相交线', 'depth': '2', 'href': '/let3/my_ppts.php?cid=290620'}...
