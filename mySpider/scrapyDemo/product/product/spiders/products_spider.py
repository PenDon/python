import scrapy
from lxml.html import etree, tostring
from ..items import ProductItem


class ProductsSpider(scrapy.Spider):
    """
    MLYJ Products Spider
    """
    name = "products"
    host = 'http://www.engraving-charms.com'

    def start_requests(self):
        urls = [
            'http://www.engraving-charms.com/products.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        # 从首页获取各个分类页面url
        tree = etree.HTML(response.text)
        tags = tree.xpath('//div[@class="n_menu_list_2"]//h2/a')[:1]
        for tag in tags:
            yield scrapy.Request(url=self.host + tag.xpath('./@href')[0], callback=self.parse_category,
                                 cb_kwargs={'category': tag.xpath('./text()')[0]})

    def parse_category(self, response, category):
        # 从分类页面获取产品详情页面url
        tree = etree.HTML(response.text)
        product_urls = tree.xpath("//li/div[@class='img']/a[@title]/@href")[:1]

        # 翻页处理
        next_element = tree.xpath("//a[@class='next disabled']")
        # if len(next_element):
        #     next_page = tree.xpath("//a[@class='next']/@href")[0]
        #     yield scrapy.Request(url=self.host + next_page, callback=self.parse_category)
        for url in product_urls:
            yield scrapy.Request(url=self.host + url, callback=self.parse_product, cb_kwargs={'category': category})

    def parse_product(self, response, category):
        # 解析产品详情页面
        tree = etree.HTML(response.text)

        item = ProductItem()
        item['name'] = tree.xpath('//div[@class="top_tip"]/h2/text()')[0]
        item['category'] = category

        # image urls, 小图替换为大图 - pm 替换为 pl
        item['images'] = ['http:' + img_url.replace('photo/pm', 'photo/pl') for img_url in
                          tree.xpath('//table[@class="fleft"]//img/@src')]
        item['desc_images'] = [self.host + img_url for img_url in
                               tree.xpath('//div[@class="details_wrap"]//img[@class="lazyi"]/@data-original')]

        table_text = tree.xpath('//*[@class="tables data"][1]//td/text()')
        item['origin_place'] = table_text[0]
        item['brand'] = table_text[1]
        item['certification'] = ''
        item['model_number'] = ''

        terms = tree.xpath('//*[@class="tables data"][2]//td/text()')
        item['min_order_quantity'] = terms[0]
        item['price'] = terms[1]
        item['package_details'] = terms[2]
        item['delivery_time'] = terms[3]
        item['payment'] = terms[4]
        item['supply_ability'] = terms[5]

        # description handle
        description = tree.xpath('//div[@class="details_wrap"]')[0]
        description = tostring(description).decode('utf-8')
        desc_imgs = tree.xpath('//div[@class="details_wrap"]//img[@class="lazyi"]/@data-original')
        for img in desc_imgs:
            # 替换 description 中的 load_icon.gif
            description = description.replace('/images/load_icon.gif', '/images/' + img.split('/')[-1], 1)
            pass
        item['description'] = description
        # self.log(item)
        yield item
