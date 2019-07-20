# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:59:06 2019

@author: DELL-1
"""

#数据库表中每列
information = ['position',
               'salary_min',
               'salary_max',
               'experience',
               'degree',
               'work_place',
               'company_name',
               'company_type',
               'company_finance',
               'company_scale',
               'bonus',
               'url']
#过滤数据
item = ['{{item.positionName}}',
        '{{item.salary}}',
        '{{item.salary}}',
        '{{item.workYear}}',
        '{{item.education}}',
        '{{item.city}}',
        '{{item.companyShortName}}',
        '{item.industryField}}',
        '{{item.financeStage}}',
        '{{item.companySize}}',
        '{{item.positionAdvantage}}',
        'https://www.lagou.com/jobs/{{item.positionId}}.html']

'''
    过滤掉相同内容的招聘信息
'''
def pass_common(data_in):
    data_in = data_in.drop_duplicates(subset=['url'])
    return data_in     
'''   
    过滤掉存在NULL和空值的数据
'''
def data_null(data_in):
    for i in range(len(information)):
        data_in = data_in[True^data_in[information[i]].isin([None])]
        data_in = data_in[True^data_in[information[i]].isin([""])]
    return data_in

'''    
    过滤掉salary_max = 1 的数据
'''
def data_salary_max(data_in):
    data_in = data_in[True^data_in['salary_max'].isin([1])]
    return data_in

'''
    过滤掉有{{item.xxxxx}}的数据
'''
def pass_item(data_in):
    for i in range(len(item)):
        data_in = data_in[True^data_in[information[i]].isin([item[i]])]
    return data_in
