# -*- coding: utf-8 -*-
# @Time     : 2022/3/14 13:42
# @Author   : 右陌
# @Software : PyCharm

# 导入
import time
import random
import re
import requests
import csv
import pymysql
# from lxml import etree
from fake_useragent import UserAgent


# 创建类
class CarSpider:

    def __init__(self):  # 初始化

        self.url = 'https://www.che168.com/china/a0_0msdgscncgpi1lto8csp{}exx0/'
        # 创建User_Agent池
        # self.header_list = [
        #     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        #     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        #     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        #     'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        #     'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50']

        # self.header = {'User-Agent': random.choice(self.header_list)}
        self.header = {'User-Agent': str(UserAgent().random)}
        # self.f = open('f:car_sp.csv', 'w', newline='', encoding='gb2312')  # csv文件路径文件名，编码方式，每行之间没有空格
        # self.writer = csv.writer(self.f)

    def get_html(self, url):  # 获取html
        html = requests.get(url=url, headers=self.header).content.decode('gb2312', 'ignore')  # 根据网页源码可以看出是gb2312
        return html

    def re_func(self, regex, html):  # 解析网页
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        return r_list

    def parse_html(self, one_url):  # 处理网页
        # 正则表达式
        one_regex = '<div class="cards-bottom">.*?<h4 class="card-name">(.*?)</h4>.*?<p class="card.*?">(.*?)</p>.*?<span class="pirce"><em>(.*?)</em>.*?</span>.*?<s>(.*?)</s>'
        one_html = self.get_html(url=one_url)  # 获取网址
        r_list = self.re_func(regex=one_regex, html=one_html)  # 解析网页
        # print(r_list)
        self.save_html(r_list)

    def save_html(self, r_list):  # 数据处理
        for i, r in enumerate(r_list):
            table = '`iecar`.`secondcar`'
            # car_id = i
            print(r)
            car_name = '\''+r[0].strip()+'\''
            car_road = '\''+r[1].split('／')[0].strip()+'\''
            car_time = '\''+r[1].split('／')[1].strip()+'\''
            car_city = '\''+r[1].split('／')[2].strip()+'\''
            car_price = '\''+r[2].strip() + '万'+'\''
            car_preprice = '\''+r[3].strip() + '\''
            car_prikey = '\''+eval(car_road+car_time)+ '\''
            keys = '`car_name`, `car_road`, `car_time`, `car_city`, `car_price`, `car_preprice`, `car_prikey`'
            # print(car_id)
            sql1 = 'INSERT INTO {table} ({keys}) VALUES ({car_name},{car_road},{car_time},{car_city},{car_price},{car_preprice},{car_prikey})'.format(table=table, keys=keys, car_name=car_name, car_road=car_road, car_time=car_time, car_city=car_city, car_price=car_price, car_preprice=car_preprice, car_prikey=car_prikey)
            print(sql1)
            cursor.execute(sql1)
            #   名称              公里数                     上牌时间                       销售者                    销售价值
            # li = [r[0].strip(), r[1].split('／')[0].strip(), r[1].split('／')[1].strip(), r[1].split('／')[3].strip(),
            #       r[2].strip() + '万']
            # print(li)
            # self.writer.writerow(li)
            print('Successful')
            db.commit()


    def run(self):
        # li = ['名称', '公里数', '上牌时间', '销售者', '价格']  # csv首行
        # self.writer.writerow(li)
        for offset in range(1, 101):
            time.sleep(random.random() * 15)
            one_url = self.url.format(offset)
            self.parse_html(one_url)
            print('|第{}页爬取成功|'.format(offset))
            time.sleep(random.uniform(3, 5))
            print('-' * 20)
        # self.f.close  # 关闭文件

# 1700


if __name__ == '__main__':
    # 使用 connect 方法，传入数据库地址，账号密码，数据库名得到数据库对象
    db = pymysql.connect(host="localhost", user="root", password="root", db="iecar", port=3306)
    # 接着获取 cursor 来操作数据库
    cursor = db.cursor()
    # sql2 = 'drop table secar'
    # cursor.execute(sql2)
    # sql = """CREATE TABLE `iecar`.`secondcar` (
    #                        `car_id` INT UNSIGNED AUTO_INCREMENT,
    #                        `car_name` VARCHAR(300) NOT NULL,
    #                        `car_road` VARCHAR(40) NOT NULL,
    #                        `car_time` VARCHAR(40) NOT NULL,
    #                        `car_city` VARCHAR(40) NOT NULL,
    #                        `car_price` VARCHAR(40) NOT NULL,
    #                        `car_preprice` VARCHAR(40) NOT NULL,
    #                        `car_energy` VARCHAR(80) NOT NULL,
    #                        `car_prikey` VARCHAR(80) NOT NULL,
    #                        PRIMARY KEY ( `car_id` ))"""
    # cursor.execute(sql)
    # update = ','.join([" {key} = %s".format(key=key) for key in data])
    # sql += update

    start_time = time.time()
    print("|执行开始|")
    print('-' * 20)
    spider = CarSpider()
    # -----------------------------------爬虫主程序
    spider.run()
    end_time = time.time()
    # 多组数据后的查重步骤
    sql = 'DELETE FROM `secondcar` WHERE `car_id` NOT IN (SELECT temp.min_id FROM (SELECT MIN(car_id) AS min_id FROM `secondcar` GROUP BY `car_prikey`) temp)'
    cursor.execute(sql)
    db.commit()
    # --------------------------------------数据处理主程序
    # 将数据库中汽车按动力类型进行分类
    cname = ['新能源','混动','小鹏','Model','哪吒','蔚来','smart','理想','小蚂蚁','EQS','大众ID','CROZZ','续航','艾瑞泽e','荣威E','电','Polestar','江淮i','AION','比亚迪e','思皓E','马自达E','欧拉','宏光E','Cayenne','微蓝']
    for cn in cname:
        sql2 = 'UPDATE `secondcar` SET car_energy=\'电\' WHERE car_name regexp (\'{cn}\') '.format(cn =cn)
        print(sql2)
        cursor.execute(sql2)
        db.commit()
    # 对剩余车辆添加油用车标签
    sql3 = 'UPDATE `secondcar` SET car_energy=\'油\' WHERE car_energy is null OR car_name regexp \'骐达\''
    cursor.execute(sql3)
    print(sql3)
    db.commit()
    # 对未上牌车辆用车时间取最近年份即2022年
    sql4 = 'UPDATE `secondcar` SET car_time=\'2022\' WHERE car_time = \'未上牌\''
    print(sql4)
    print('|执行结束|')
    print('-' * 20)
    # print('|总共执行时间为：{0:.2f}秒|'.format(end_time - start_time))

