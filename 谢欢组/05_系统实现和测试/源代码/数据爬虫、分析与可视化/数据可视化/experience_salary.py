# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:41:56 2019

@author: DELL-1
"""

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

def experience_salary(get_all_data):
    experience_salary = {}
    experience = list(get_all_data['experience'].value_counts().index)
    for i in range(len(experience)):
        get_experience = get_all_data[False^get_all_data['experience'].str.contains(experience[i])]
        experience_salary[experience[i]] = ((get_experience['salary_max']+get_experience['salary_min'])/2).mean()
    dicts = {}
    experiences = ['经验不限',
           '经验应届毕业生',
           '经验1年以下',
           '经验1-3年',
           '经验3-5年',
           '经验5-10年',
           '经验10年以上']
    for e in experiences:
        dicts[e] = experience_salary[e]

    attr = dicts.keys()
    value = dicts.values()
    color = ['red',
             'orange',
             'yellow',
             'green',
             '#48D1CC',
             'blue',
             'purple']
    plt.figure(figsize=(10,10))
    plt.bar(attr,
            value,
            color = color,
            edgecolor='black')
    for a,b in zip(attr,value):
        plt.text(a,b+0.4,'%.2f'%b,ha='center',va='bottom',fontsize=20)
    plt.xlabel('工作经验',fontsize = 20)
    plt.ylabel('平均薪资（单位：千元）',fontsize = 20)
    plt.title('工作经验与平均薪资的关系',fontsize = 20)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=20)
    plt.savefig("C:/WeSite/DataCharts/薪资关联/经验要求与薪资水平-100dpi.jpg")
    #plt.show()