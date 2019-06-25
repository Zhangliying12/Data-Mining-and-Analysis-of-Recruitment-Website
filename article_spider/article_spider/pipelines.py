# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import re

import MySQLdb

class ArticleSpiderPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'root', 'job_info', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):

        j = -1
        for i in range(len(item['position'])):
            item['experience_and_degree'][i] = item['experience_and_degree'][j + 3]
            j = j + 3

        for i in range(len(item["position"])):
            position = item["position"][i]
            salary = item['salary'][i]

            salary_min = re.findall("^(\d.*)k-", salary)[0]
            salary_max = re.findall("-(\d.*)k", salary)[0]

            print(salary_min)
            print(type(salary_min))
            experience_and_degree = item['experience_and_degree'][i]
            experience = re.findall("(.*) /",experience_and_degree)[0]
            degree = re.findall("/ (.*)",experience_and_degree)[0]

            work_place = item['work_place'][i]
            work_place = re.findall("(.*)·",work_place)[0]

            company_name = item['company_name'][i]

            industry = item['industry'][i]
            company_type = re.findall("\s*(.*?)\s*[/]",industry)[0]
            #company_type = re.findall("(.*?)[/]",company_type)
            company_finance = re.findall("/\s(.*?)\s/",industry)[0]
            company_scale = re.findall("[/].*?[/]\s*(.*)",industry)[0]
            #company_scale = re.findall("")

            bonus = re.findall('“(.*?)”',item['bonus'][i])[0]

            url = item['url'][i]

            insert_sql = """
                        insert into ai(position, salary_min, salary_max, experience, degree, work_place, company_name, company_type, company_finance, company_scale, bonus,url)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
            self.cursor.execute(insert_sql, (position, int(salary_min), int(salary_max), experience, degree, work_place, company_name, company_type, company_finance, company_scale, bonus, url))
            self.conn.commit()

            print("职位名称：    ",position)
            print("薪资范围：    ",salary)
            print("工作经历要求：",experience)
            print("学位要求：    ",degree)
            print("工作地点：    ",work_place)
            print("公司名称：    ",company_name)
            print("公司类型：    ",company_type)
            print("公司融资情况：",company_finance)
            print("公司规模：    ",company_scale)
            print("福利待遇：    ",bonus)
            print("招聘链接：    ",url)
            print("\n")

        return item

"""
            insert_sql = "
                        insert into all(position, salary_min, salary_max)
                        VALUES (%s, %s, %s)
                    "
            self.cursor.execute(insert_sql, (title,salary_min,salary_max))
            self.conn.commit()
"""


