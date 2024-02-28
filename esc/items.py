# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class carItem(scrapy.Item):
    # define the fields for your item here like:
    # Car_id = scrapy.Field()  # id
    ID = scrapy.Field()
    Brand = scrapy.Field()  # 品牌 y
    Series = scrapy.Field()  # 型号 y
    Province = scrapy.Field()  # 省/自治区/直辖市 y
    City = scrapy.Field()  # 城市 y
    Gears = scrapy.Field()  # 档位
    Price = scrapy.Field()  # 价格
    Age = scrapy.Field()  # 车龄
    Mileage = scrapy.Field()  # 里程
    # Standard = scrapy.Field()  # 排放标准
    Displacement = scrapy.Field()  # 排量
    Engine = scrapy.Field()  # 发动机
    # Grade = scrapy.Field()  # 车辆级别
    Color = scrapy.Field()  # 车身颜色
    Fuel = scrapy.Field()  # 燃油标号
    Driver = scrapy.Field()  # 驱动方式
    Inspection = scrapy.Field()  # 年检到期

    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    msg = scrapy.Field()
    nowpri = scrapy.Field()
    newpri = scrapy.Field()
    pass
