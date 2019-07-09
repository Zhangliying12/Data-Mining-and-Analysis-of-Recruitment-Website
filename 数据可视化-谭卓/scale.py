# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:31:50 2019

@author: DELL-1
"""
import collections

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

def company_scale(get_data_all):
    scale = [
        '少于15人',
        '15-50人',
        '50-150人',
        '150-500人',
        '500-2000人',
        '2000人以上'
    ]
    plt.figure(figsize=[12,12])

    data_dict = collections.Counter(get_data_all['company_scale'])
    data_dict_ord = collections.OrderedDict()

    for e in scale:
        data_dict_ord[e] = data_dict[e]

    sizes = data_dict_ord.values()
    labels = data_dict_ord.keys()
    colors = ['springgreen', 'lightgrey', 'lightskyblue', 'yellow', 'peachpuff', 'cyan']
    patches, text1, text2 = plt.pie(sizes,
                          labels=labels,
                          colors=colors,
                          labeldistance = 1.1,#图例距圆心半径倍距离
                          autopct = '%3.2f%%', #数值保留固定小数位
                          shadow = False, #无阴影设置
                          startangle =90, #逆时针起始角度设置
                          pctdistance = 0.6) #数值距圆心半径倍数距离

    for t in text1:
        t.set_size(20)
    for t in text2:
        t.set_size(20)
    plt.axis('equal')
    # # 设置图例标题文字大小
    # plt.rcParams.update({'font.size': 15})
    # plt.legend(title="公司规模统计饼状图",
    #            loc=1,
    #            prop={'family':'SimHei','size':10})
    #plt.title("公司规模统计",fontsize = 30)
    plt.savefig('C:/WeSite/DataCharts/公司概况/公司规模统计饼状图-100dpi.jpg', dpi=100)
    #plt.show()