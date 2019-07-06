# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:14:13 2019

@author: DELL-1
"""


import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

def company_scale_salary(get_all_data):
    company_salary = {}
    company_scale = list(get_all_data['company_scale'].value_counts().index)
    
    for i in range(len(company_scale)):
        get_company = get_all_data[False^get_all_data['company_scale'].str.contains(company_scale[i])]
        company_salary[company_scale[i]] = ((get_company['salary_max']+get_company['salary_min'])/2).mean()

    dicts = {}
    scale = [
        '少于15人',
        '15-50人',
        '50-150人',
        '150-500人',
        '500-2000人',
        '2000人以上',
        '少于15人'
    ]

    for s in scale:
        dicts[s] = company_salary[s]

    color = ['red',
             'orange',
             'yellow',
             'green',
             '#48D1CC',
             'blue',
             'purple',
             '#4A4A4A']
    attr = dicts.keys()
    value = dicts.values()
    plt.figure(figsize=(10,10))
    plt.bar(attr,
            value,
            color = color,
            edgecolor='black')
    for a,b in zip(attr,value):
        plt.text(a,b+0.3,'%.2f'%b,ha='center',va='bottom')
    plt.xlabel('公司规模')
    plt.ylabel('平均薪资')
    plt.title('公司规模与平均薪资关系图')

    plt.savefig("C:/WeSite/DataCharts/薪资关联/公司规模与薪资水平-100dpi.jpg")
    plt.show()