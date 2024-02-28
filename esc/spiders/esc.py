from urllib.parse import urljoin
import scrapy
from esc.items import carItem
# from esc.settings import ipPool
import random
import requests

class escSpider(scrapy.Spider):
    name = 'car'
    total_pages = 100
    allowed_domains = ["che168.com"]
    start_urls = ['https://www.che168.com/china/a0_0msdgscncgpi1lto8csp100exx0/']

    def start_requests(self):
        print('START')
        for linkurl in range(self.total_pages-1, 1, -1):
            self.start_urls.append('https://www.che168.com/china/a0_0msdgscncgpi1lto8csp{lin}exx0/'.format(lin=linkurl))
        print(self.start_urls)
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # 在源文件中查找子链接
        links = response.xpath('//li[@class="cards-li list-photo-li "]/a/@href').extract()
        for link in links:
            link = link.split('?')[0]
            link = urljoin('https://www.che168.com', link)
            print(link)
            # 依次访问子链接并提取内容
            yield scrapy.Request(url=link, callback=self.parse_sub_link, dont_filter=True)


    def parse_sub_link(self, response):
        print(response.url)
        car_item = carItem()
        id = response.xpath('//meta[@http-equiv="mobile-agent"]/@content').extract()[0]
        id = str(id).split('.html')[0][-8:]
        if id.isdigit():
            car_item['ID'] = id
            print(id)
            # 价格 型号
            mss = str(response.xpath('//title/text()').extract())
            if '_' in mss:
                series = mss.split('】')[1].split(' ')[0]
                price = mss.split('_')[1].split('_')[0]
                car_item['Price'] = price
                car_item['Series'] = series
                # 省市
                location = response.xpath('//meta[@name="location"]/@content').extract()[0]
                province = location.split('province=')[1].split(';')[0]

                if province == "北京" or province == "重庆" or province == "天津" or province == "上海":
                    brand = str(response.xpath('//div[@class="bread-crumbs content"]/a[3]/text()').extract())
                    brand = brand[2:-2]
                    brand = brand[2:]
                else:
                    brand = str(response.xpath('//div[@class="bread-crumbs content"]/a[4]/text()').extract())
                    brand = brand[2:-2]
                    brand = brand[2:]
                car_item['Province'] = province
                car_item['Brand'] = brand

                # 里程 车龄 档位 排量 排放标准
                msg = response.xpath('//div[@class="car-box"]')
                li = msg.xpath('./ul[@class="brand-unit-item fn-clear"]')
                mileage = li.xpath('./li[1]/h4/text()').extract()
                mileage = str(mileage).split('\'')[1].split('\'')[0]
                mileage = float(mileage[:-3])
                car_item['Mileage'] = mileage
                if str(li.xpath('./li[2]/h4/text()').extract()).split('\'')[1][0].isdigit():
                    shangpai = int(str(li.xpath('./li[2]/h4/text()').extract()).split('\'')[1][0:4])
                    age = 2023 - shangpai
                    car_item['Age'] = age
                else:
                    car_item['Age'] = 0

                gears_displacement = str(li.xpath('./li[3]/h4/text()').extract())
                gears = gears_displacement.split(' / ')[0]
                gears = str(gears).split('\'')[1]
                displacement = gears_displacement.split(" / ")[1]
                displacement = str(displacement).split('\'')[0]
                car_item['Gears'] = gears
                car_item['Displacement'] = displacement
                engine = response.xpath('//div[@class="all-basic-content fn-clear"]/ul[3]/li[1]/text()').extract()
                engine = str(engine).split('\'')[1].split('\'')[0]
                color = response.xpath('//div[@class="all-basic-content fn-clear"]/ul[3]/li[3]/text()').extract()
                color = str(color).split('\'')[1].split('\'')[0]
                driver = response.xpath('//div[@class="all-basic-content fn-clear"]/ul[3]/li[5]/text()').extract()
                driver = str(driver)
                if '驱' not in driver:
                    driver = str(
                        response.xpath('//div[@class="all-basic-content fn-clear"]/ul[3]/li[4]/text()').extract())
                driver = driver.split('\'')[1].split('\'')[0]
                car_item['Driver'] = driver
                car_item['Color'] = color
                car_item['Engine'] = engine

                yield car_item