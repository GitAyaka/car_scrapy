# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openpyxl import Workbook


import json, codecs, os, csv
class EscPipeline:
    # def __init__(self):
    #     self.wb = Workbook()
    #     self.ws = self.wb.active
    #     self.ws.append(['型号', '信息', '新车价格', '当前价格'])
    #
    #     # self.f = open("./二手车1.csv", mode="a", encoding="utf-8")
    #     # self.f.append(['型号', '信息', '当前价格', '新车价格'])
    #
    # def open_spider(self, spider):
    #     pass
    #
    # def close_spider(self, spider):
    #     # if self.ws:
    #     #     self.ws.close()
    #     pass
    #
    # def process_item(self, item, spider):
    #     line = [item['title'], item['msg'], item['newpri'], item['nowpri']]
    #     self.ws.append(line)
    #     self.wb.save('二手车.xlsx')
    #     # txt = str.format('{},{},{},{}\n',item['title'],item['msg'],item['newpri'],item['nowpri'])
    #     # self.ws.write(txt)
    #     return item




# # 保存为json文件
# class JsonPipeline(object):
#     def __init__(self):
#         # 文件的位置
#         store_file = os.path.dirname(__file__) + '/spiders/car.json'
#         # 打开文件，设置编码为utf-8
#         self.file = codecs.open(filename=store_file, mode='wb', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + ',\n'
#         # 逐行写入
#         self.file.write(line)
#         return item
#
#     def close_spider(self, spider):
#         self.file.close()


# 保存为csv文件
# class csvPipiline(object):
    def __init__(self):
        # 文件的位置
        store_file = os.path.dirname(__file__) + '/spiders/data.csv'
        # 打开文件，并设置编码
        self.file = codecs.open(filename=store_file, mode='wb', encoding='utf-8')
        # 写入csv
        self.writer = csv.writer(self.file)
        line = ('ID', 'Brand', 'Series', 'Province', 'Gears',
                'Price', 'Age', 'Mileage',
                # 'Standard',
                'Displacement',
                'Engine',
                # 'Grade',
                'Color', 'Driver')
        self.writer.writerow(line)

    def process_item(self, item, spider):
        line = (item['ID'], item['Brand'], item['Series'],  item['Province'], item['Gears'],
                item['Price'], item['Age'], item['Mileage'],
                # item['Standard'],
                item['Displacement'],
                item['Engine'],
                # item['Grade'],
                item['Color'], item['Driver'])
        self.writer.writerow(line)
        return item

    def close_spider(self, spider):
        self.file.close()
