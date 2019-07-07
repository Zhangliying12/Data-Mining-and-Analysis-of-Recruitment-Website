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
    wedges, texts, autotexts = plt.pie(x = value,
                                       labels = attr,
                                       autopct = "%.2f%%",
                                       colors = colors,
                                       shadow = False)
    plt.legend(wedges,
               attr,
               fontsize = 12,
               title='学历分布',
               loc = 'center left',
               bbox_to_anchor = (1,0,0.15,1.7)
               )
    plt.axis('equal')
    plt.title('学历需求',fontsize = 20)
    plt.savefig('C:/WeSite/DataCharts/岗位概况/相关要求/学历要求分布饼状图-100dpi.jpg', dpi=100)
    plt.show()
