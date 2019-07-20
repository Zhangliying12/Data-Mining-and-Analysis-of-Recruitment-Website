# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:19:41 2019

@author: DELL-1
"""
import collections

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

def finance(get_all_data):
    finance = [
        '不需要融资',
        '未融资',
        '天使轮',
        'A轮',
        'B轮',
        'C轮',
        'D轮及以上',
        '上市公司'
    ]
    plt.figure(figsize=[13,13])
    data_dict = collections.Counter(get_all_data['company_finance'])
    data_dict_ord = collections.OrderedDict()

    for e in finance:
        data_dict_ord[e] = data_dict[e]

    sizes = data_dict_ord.values()
    labels = data_dict_ord.keys()
    print("公司融资统计")
    print(sizes)
    print(labels)
    colors = ['springgreen','yellowgreen','lightskyblue','yellow','peachpuff','seashell','cyan','lightgrey']
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
    #plt.rcParams.update({'font.size': 20})
    #plt.legend(loc=0,prop={'family': 'SimHei', 'size': 20})
    #plt.title('融资分布',fontsize = 30)
    plt.savefig('C:/WeSite/DataCharts/公司概况/公司融资情况分析-100dpi.jpg', dpi=100)
    #plt.show()