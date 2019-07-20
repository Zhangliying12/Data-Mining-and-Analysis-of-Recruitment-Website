# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:58:36 2019

@author: DELL-1
"""

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

def finance_salary(get_all_data):
    finance_salary = {}
    finance = list(get_all_data['company_finance'].value_counts().index)
    for i in range(len(finance)):
        get_finance = get_all_data[False^get_all_data['company_finance'].str.contains(finance[i])]
        finance_salary[finance[i]] = ((get_finance['salary_max']+get_finance['salary_min'])/2).mean()
    finances = [
        '不需要融资',
        '未融资',
        '天使轮',
        'A轮',
        'B轮',
        'C轮',
        'D轮及以上',
        '上市公司'
    ]

    dicts = {}
    for f in finances:
        dicts[f] = finance_salary[f]

    attr = dicts.keys()
    value = dicts.values()
    print("融资情况-薪资")
    print(attr)
    print(value)
    plt.figure(figsize=(10,10))
    color = ['red',
             'orange',
             'yellow',
             'green',
             '#48D1CC',
             'blue',
             'purple',
             '#4A4A4A'] 
    plt.bar(attr,
            value,
            width = 0.6,
            color = color,
            edgecolor='black')
    for a,b in zip(attr,value):
        plt.text(a,b+0.2,'%.2f'%b,ha='center',va='bottom',fontsize = 20)
    plt.xlabel('公司融资类型',fontsize = 20)
    plt.ylabel('平均薪资（单位：千元）',fontsize = 20)
    plt.title('融资情况与平均薪资的关系',fontsize = 20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=20)
    plt.savefig("C:/WeSite/DataCharts/薪资关联/融资情况与薪资水平-100dpi.jpg")
    #plt.show()