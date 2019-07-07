# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:22:16 2019

@author: DELL-1
"""

import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

def degree_salary(get_all_data):
    plt.figure(figsize=[10, 10])
    degree_salary = {}
    degree = list(get_all_data['degree'].value_counts().index)
    for i in range(len(degree)):
        get_degree = get_all_data[False^get_all_data['degree'].str.contains(degree[i])]
        degree_salary[degree[i]] = ((get_degree['salary_max']+get_degree['salary_min'])/2).mean()

    degree = [
        '不限',
        '大专',
        '本科',
        '硕士',
        '博士'
    ]
    dicts = {}
    for d in degree:
        dicts[d] = degree_salary[d]
    attr = dicts.keys()
    value = dicts.values()

    color = ['red',
             'orange',
             'yellow',
             'green',
             '#48D1CC']
    plt.bar(attr,
            value,
            width = 0.6,
            color = color,
            edgecolor = 'black')
    for a,b in zip(attr,value):
        plt.text(a,b+0.4,'%.2f'%b,ha = 'center',va = 'bottom',fontsize = 20)


    plt.xlabel('个人学历',fontsize = 20)
    plt.ylabel('平均薪资',fontsize = 20)
    plt.title('个人学历与平均薪资的关系',fontsize = 20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.savefig("C:/WeSite/DataCharts/薪资关联/学历与薪资水平-100dpi.jpg")
    plt.show()