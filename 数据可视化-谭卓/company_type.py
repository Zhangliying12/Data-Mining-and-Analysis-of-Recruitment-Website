# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:16:42 2019

@author: DELL-1
"""

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

def company_type(get_all_data):
    keyword = ['移动互联网','金融','电商','企业服务','数据服务','文娱丨内容',
               '游戏','硬件','消费生活','信息安全','人工智能','社交','教育',
               '医疗丨健康','广告营销','移动开发','通讯电子','汽车丨出行',
               '物联网','O2O','房产家居','软件开发','区块链','电子商务','旅游',
               'VR丨AR','物流丨运输','工具','体育','大数据','文化娱乐','生活服务',
               '其他','不限']
    get_all_data = get_all_data['company_type']
    company_type = {}
    count = 0
    
    for i in range(len(keyword)):
        temp = get_all_data.str.contains(keyword[i])
        value = list(temp.values)
        for j in range(len(value)):
            if value[j] == True:
                count = count + 1        
        company_type[keyword[i]] = count
        count = 0
    company_type = dict(sorted(company_type.items(),key=lambda x:x[1],reverse = True))
    
    attr_temp = list(company_type.keys())
    value_temp = list(company_type.values())
    print("公司类型-数量")
    print(attr_temp)
    print(value_temp)
    plt.figure(figsize=(10,10))
    color = ['red',
             'orange',
             'yellow',
             'green',
             '#48D1CC',
             'blue',
             'purple',
             '#4A4A4A',
             '#A52A2A',
             '#7171C6'] 
    plt.bar(attr_temp[:10],
            value_temp[:10],
            color = color,
            edgecolor = 'black')
    for a,b in zip(attr_temp[:10],value_temp[:10]):
        plt.text(a,b+0.6,b,ha='center',va='bottom',fontsize = 20)
    plt.xlabel("公司类型",fontsize=20)
    plt.ylabel("数量",fontsize=20)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=20)
    plt.title("公司类型-数量关系图",fontsize=20)
    plt.savefig('C:/WeSite/DataCharts/公司概况/不同公司类型柱状图-100dpi.jpg',dpi=100)
    #plt.show()
