# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from os import path
from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
import os
from urllib.parse import urlparse
from myLib.mysql import Mysql

from typing import List, Tuple


class ProductPipeline(ImagesPipeline):
    """
    图片下载中间件
    """

    def file_path(self, request, response=None, info=None, **kwargs):
        """
        图片保存时的文件名
        :param request:
        :param response:
        :param info:
        :return:
        """
        return os.path.basename(urlparse(request.url).path)

    def get_media_requests(self, item, info):
        """
        从 item 中获取图片 url 并发起请求
        :param item:
        :param info:
        :return:
        """
        adapter = ItemAdapter(item)
        for desc_image in adapter['desc_images']:
            filename = desc_image.split('/')[-1]
            if os.path.exists('images/' + filename):
                continue
            else:
                yield Request(desc_image)
        for product_image in adapter['images']:
            filename = product_image.split('/')[-1]
            if os.path.exists('images/' + filename):
                continue
            else:
                yield Request(product_image)
        # @todo change the image url to localhost

    def item_completed(self, results: List[Tuple[bool, dict]], item, info):
        """
        图片下载完成后需要进行的额外处理, 必须返回一个 item 或修改后的 item
        :param results: [(True, {'url': 'ima_url', 'path': 'xxx.jpg', 'checksum': 'd9e8a7f3fae9d13fdfcfab198abb4e56',
        'status': 'downloaded'})
        :param item:
        :param info:
        :return:
        """
        result_list = [result for success, result in results if success]
        adapter = ItemAdapter(item)
        product_images = []
        desc_images = []
        for result in result_list:
            if result['url'] in adapter['images']:
                product_images.append('/images/' + result['path'])
                continue
            if result['url'] in adapter['desc_images']:
                desc_images.append('/images/' + result['path'])

        adapter['images'] = product_images
        adapter['desc_images'] = desc_images

        return item


class MysqlPipeline:
    """
    图片下载完成后, 将所有数据入库 - Mysql or Json
    @todo sql批量插入
    """
    item_list = []
    item_length = 100

    def __init__(self):
        self.mysql = Mysql(dbName='dbname')

    def process_item(self, item, spider):
        """
        数据入库处理
        :param item:
        :param spider:
        :return:
        """
        self.mysql.insert('product', [item['name'], item['category']], ['name', 'category'])
        product_id = self.mysql.cursor.lastrowid
        self.mysql.batch_insert('product_image', [[product_id, img] for img in item['images']],
                                ['product_id', 'real_path'])
        self.mysql.batch_insert('product_description_image', [[product_id, img] for img in item['desc_images']],
                                ['product_id', 'real_path'])
        self.mysql.conn.commit()
        return item
