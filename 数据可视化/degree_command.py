# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 17:09:09 2019

@author: DELL-1
"""

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False


def degree_command(get_all_data):
    get_all_data = get_all_data["degree"].value_counts()

    degree = [
        '不限',
        '大专',
        '本科',
        '硕士',
        '博士'
    ]

    get_all_data_ord = {}

    for d in degree:
        get_all_data_ord[d] = get_all_data[d]
    attr = get_all_data_ord.keys()
    value = get_all_data_ord.values()
    colors = ['springgreen','yellowgreen','lightskyblue','yellow','peachpuff']

    plt.figure(figsize=[10,10])
    plt.axes(aspect = 1)
    wedges, texts, autotexts = plt.pie(value,
                          labels=degree,
                          colors=colors,
                          labeldistance = 1.1,#图例距圆心半径倍距离
                          autopct = '%3.2f%%', #数值保留固定小数位
                          shadow = False, #无阴影设置
                          startangle =90, #逆时针起始角度设置
                          pctdistance = 0.6) #数值距圆心半径倍数距离
    plt.axis('equal')
    # 设置图例标题文字大小
    plt.rcParams.update({'font.size': 15})
    plt.legend(title="学历需求",
               loc=1,
               prop={'family': 'SimHei', 'size': 15})
    plt.axis('equal')
    plt.title('学历需求',fontsize = 20)
    plt.savefig('C:/WeSite/DataCharts/岗位概况/相关要求/学历要求分布饼状图-100dpi.jpg', dpi=100)
    #plt.show()
