# MLYJ Product Spider

import requests
from lxml.html import etree, tostring
import time
from myLib.header import get_header
from myLib.mysql import Mysql
import os

"""
Start with product categories page, page url rules: suffix "p1 - p2 -p3", according to whether next button has class 
named "disable" (xpath express //a[@class="next disabled"]) 
"""

page_param = "p3"

host_url = 'http://www.engraving-charms.com'
product_category_url = f'{host_url}/supplier-417894{page_param}-custom-shaped-keychains'
product_category = 'Custom Shaped Keychains'

h = get_header()
# @todo request with session
# use proxy
# res = requests.get(
#     product_category_url,
#     proxies={'https': 'http://127.0.0.1:11000', 'http': 'http://127.0.0.1:11000'}, headers=get_header())


# normal request for test
res = requests.get(product_category_url, headers=h)
# res = requests.get(product_category_url, proxies={'https': 'http://127.0.0.1:11000', 'http': 'http://127.0.0.1:11000'}, headers=h)

if res.status_code != 200:
    print(res.content)
    exit(0)
tree = etree.HTML(res.content)
product_results = []
product_image_results = []
product_desc_image_results = []

product_hrefs = tree.xpath("//li/div[@class='img']/a[@title]/@href")
product_id = 274
product_image_id = 1192
product_desc_image_id = 706
time.sleep(1)
print(f"产品共{len(product_hrefs)}个")
print(h)
for product_href in product_hrefs:
    href = host_url + product_href
    product_res = requests.get(href, headers=h)
    # product_res = requests.get(href, headers=h, proxies={'https': 'http://127.0.0.1:11000', 'http': 'http://127.0.0.1:11000'})

    tree = etree.HTML(product_res.content)
    print("正在获取产品" + str(product_id))
    table_data = tree.xpath('//table[@class="tables data"]//td/text()')
    product_name = tree.xpath('//div[@class="top_tip"]/h2/text()')[0]
    print(product_name)
    desc_imgs = tree.xpath('//div[@class="details_wrap"]//img[@class="lazyi"]/@data-original')
    product_description = tree.xpath('//div[@class="details_wrap"]')[0]
    product_description = tostring(product_description).decode('utf-8')
    for img in desc_imgs:
        product_description = product_description.replace('load_icon.gif', 'images/' + img.split('/')[-1], 1)
        try:
            desc_img_res = requests.get(host_url + img, headers=h)
        except Exception as e:
            continue
        # desc_img_res = requests.get(host_url + img, headers=h, proxies={'https': 'http://127.0.0.1:11000', 'http': 'http://127.0.0.1:11000'})

        filename = img.split('/')[-1]
        if not os.path.exists('images/' + filename):
            with open('images/' + filename, 'wb') as f:
                f.write(desc_img_res.content)
        product_desc_image_results.append([product_desc_image_id, product_id, 'images/' + filename])
        product_desc_image_id += 1
        time.sleep(1)

    product_images = tree.xpath('//table[@class="fleft"]//img/@src')

    """
    database filed: id name certification origin_place brand model_number min_order_quantity price package_details 
    delivery_time payment supply_ability description 
    
    category: custom-engraving-charms  
    table_data: ['China', 'Mylongingcharm', '100 PCS', 'Negotiable', 'Carton Packing, PP bag', '5 - 8 working days', 'Western 
    Union, MoneyGram, T/T', '50000 / months'] 
    """
    insert_data = [product_id, product_name, product_category]
    while len(table_data) < 10:
        table_data.insert(2, '')
    insert_data.extend(table_data)
    insert_data.append(product_description)

    if len(insert_data) != 14:
        print(insert_data[:8])
        exit(0)
    product_results.append(insert_data)
    for product_image in product_images:
        product_image = product_image.replace('photo/pm', 'photo/pl')
        img_res = requests.get("http:" + product_image, headers=h)
        # img_res = requests.get("http:" + product_image, headers=h, proxies={'https': 'http://127.0.0.1:11000', 'http': 'http://127.0.0.1:11000'})

        filename = product_image.split('/')[-1]
        if not os.path.exists('images/' + filename):
            with open(f'images/{filename}', 'wb') as f:
                f.write(img_res.content)
        product_image_results.append([product_image_id, product_id, 'images/' + filename])
        product_image_id += 1
        time.sleep(1)

    product_id += 1
    time.sleep(1)

# db config
conn = Mysql(dbName='dbname')
# conn.batch_insert()

conn.batch_insert('product', product_results)
conn.batch_insert('product_image', product_image_results)
conn.batch_insert('product_description_image', product_desc_image_results)
conn.conn.commit()
