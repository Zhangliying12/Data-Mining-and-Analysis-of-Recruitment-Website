# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:33:29 2019

@author: DELL-1
"""


import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False


def shixi(get_all_data):
    get_shixi = get_all_data[False^get_all_data['position'].str.contains('实习')]
    get_notshixi = get_all_data[True^get_all_data['position'].str.contains('实习')]

    plt.figure(figsize=[10,10])
    labels = ['实习','非实习']
    value = [len(get_shixi),len(get_notshixi)]
    explode = [0.1,0]
    color = ['cyan','peachpuff']
    plt.axes(aspect =1)
    plt.pie(value,
            labels = labels,
            colors = color,
            explode = explode,
            autopct = '%.2f%%',
            shadow = True)
    
    plt.legend(loc='center left',
               bbox_to_anchor = (0.9,0,0,1.7),
               shadow = True,
               title = '岗位总数:'+str(len(get_shixi)+len(get_notshixi))+'\n'+
                       '实习岗位数:'+str(len(get_shixi))+'\n'+
                       '非实习岗位:'+str(len(get_notshixi))
                )
    plt.savefig('C:/WeSite/DataCharts/岗位概况/实习/整体数据分布饼状图-100dpi.jpg', dpi=100)
    plt.show()
