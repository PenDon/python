# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    images = scrapy.Field()
    desc_images = scrapy.Field()
    category = scrapy.Field()
    origin_place = scrapy.Field()
    brand = scrapy.Field()
    certification = scrapy.Field()
    model_number = scrapy.Field()
    min_order_quantity = scrapy.Field()
    price = scrapy.Field()
    package_details = scrapy.Field()
    delivery_time = scrapy.Field()
    payment = scrapy.Field()
    supply_ability = scrapy.Field()
    description = scrapy.Field()
    pass
