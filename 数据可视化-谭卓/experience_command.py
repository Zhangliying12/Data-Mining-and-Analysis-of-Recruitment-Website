# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:51:57 2019

@author: DELL-1
"""

import matplotlib.pyplot as plt
import matplotlib
import collections as cl

matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

def experience_command(get_all_data):
#get_all_data = get_all_data["experience"].value_counts()\
    get_all_data = cl.Counter(get_all_data['experience'])


    experience = ['经验不限',
       '经验应届毕业生',
       '经验1年以下',
       '经验1-3年',
       '经验3-5年',
       '经验5-10年',
       '经验10年以上']
    value = []
    for i in range(len(experience)):
        value.append(get_all_data[experience[i]])

    colors = ['yellow','yellowgreen','lightskyblue','springgreen','cyan','peachpuff','seashell']

    print("经验需求")
    print(experience)
    print(value)
    plt.figure(figsize=(10,10))
    plt.axes(aspect = 1)
    wedges, texts, autotexts = plt.pie(value,
                          labels=experience,
                          colors=colors,
                          labeldistance = 1.1,#图例距圆心半径倍距离
                          autopct = '%3.2f%%', #数值保留固定小数位
                          shadow = False, #无阴影设置
                          startangle =90, #逆时针起始角度设置
                          pctdistance = 0.6) #数值距圆心半径倍数距离
    plt.legend(wedges,
               experience,
               fontsize = 12,
               title='经验情况分布',
               loc = 'center left',
               bbox_to_anchor = (1,0,0.15,1.7)
               )
    plt.axis('equal')
    plt.title('经验需求',fontsize = 20)

    plt.savefig('C:/WeSite/DataCharts/岗位概况/相关要求/工作经验要求分布饼状图-100dpi.jpg',dpi=100,bbox_inches = 'tight')
    #plt.show()
