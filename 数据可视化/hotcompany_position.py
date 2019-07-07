# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 08:57:53 2019

@author: DELL-1
"""

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

def hotcompany_position(get_all_data):
    get_all_data = get_all_data['company_name'].value_counts()
    
    hotcompany_position = {}
    for i in range(0,20):
        hotcompany_position[(get_all_data.index)[i]] = (get_all_data.values)[i]

    hotcompany_position['上海中软'] = hotcompany_position.pop('上海中软华腾软件系统有限公司')
    hotcompany_position = dict(sorted(hotcompany_position.items(),key=lambda d:d[1],reverse=True))
    attr = hotcompany_position.keys()
    value = hotcompany_position.values()
    
    plt.figure(figsize=(10,10))
    
    plt.bar(attr,
            value,
            edgecolor='black')
    for a,b in zip(attr,value):
        plt.text(a,b+0.6,b,ha='center',va='bottom',fontsize = 20)
    #plt.xlabel("公司名",fontsize = 20)
    plt.ylabel("岗位数量",fontsize = 20)
    plt.title("公司岗位数量TOP20",fontsize = 20)
    plt.xticks(rotation=90)
    plt.yticks(fontsize = 20)
    plt.savefig('C:/WeSite/DataCharts/公司概况/公司岗位数量TOP20柱状图-100dpi.jpg', dpi=100)
    plt.show()
