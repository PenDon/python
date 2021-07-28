import requests
from lxml import etree

page_url = 'https://haokan.baidu.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/74.0.3729.157 Safari/537.36',
}

res = requests.get(page_url, headers=headers)
# print(res.text)
dom = etree.HTML(res.text)

card_lists = dom.xpath('//div[@class="card"]')
video_lists = []

print(card_lists[0].getchildren())
print(card_lists)
exit(0)

for card_li in card_lists:
    video_name = card_li.xpath('./@title')[0]
    video_page = page_url + card_li.xpath('./a[@class="card-item-link"]/@href')[0]
    video_dict = {
        'video_name':video_name,
        'video_page':video_page
    }
    video_lists.append(video_dict)

content_lists = dom.xpath('//div[@class="content"]/div[@class="cardinner card"]')

for content_div in content_lists:
    content_lis = content_div.xpath('./ul[@class="card-list clear"]/li[@class="card-item"]')
    for content_li in content_lis:
        video_name = content_li.xpath('./@title')[0]
        video_page = page_url + content_li.xpath('./a[@class="card-item-link"]/@href')[0]
        video_dict = {
                    'video_name': video_name,
                    'video_page': video_page
                }
        video_lists.append(video_dict)

print(video_lists)