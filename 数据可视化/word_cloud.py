# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:23:43 2019

@author: DELL-1
"""

import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['font.family']='sans-serif'
plt.rcParams['axes.unicode_minus'] = False

def cloud_company_type(get_all_data):
    cloud_company_type = open('cloud_company_type.txt','w',encoding='utf-8')
    get_all_data = list(get_all_data['company_type'])
    for i in range(len(get_all_data)):
        cloud_company_type.write(get_all_data[i])
    cloud_company_type.close() 
        
    get_text = open('cloud_company_type.txt','r',encoding='utf-8').read()
    cut_text = " ".join(jieba.cut(get_text))
    wordcloud = WordCloud(font_path="C:/Windows/Fonts/STKAITI.TTF",
                          background_color = 'white',
                          width = 1000,
                          height = 800)
    wordcloud = wordcloud.generate(cut_text)
    plt.imshow(wordcloud,interpolation = 'bilinear')
    plt.axis('off')
    plt.savefig('C:/WeSite/DataCharts/公司概况/公司类型词云.jpg',dpi=100)
    plt.show()
def cloud_company_bonus(get_all_data):
    cloud_company_bonus = open('cloud_company_bonus.txt','w',encoding='utf-8')
    get_all_data = list(get_all_data['bonus'])
    for i in range(len(get_all_data)):
        cloud_company_bonus.write(get_all_data[i])
    cloud_company_bonus.close()
    
    get_text = open('cloud_company_bonus.txt','r',encoding='utf-8')
    cut_text = " ".join(get_text)
    wordcloud = WordCloud(font_path = "C:/Windows/Fonts/STKAITI.TTF",
                          background_color = 'white',
                          width = 1000,
                          height = 800)
    wordcloud = wordcloud.generate(cut_text)
    plt.imshow(wordcloud,interpolation = 'bilinear')
    plt.axis('off')
    plt.savefig('C:/WeSite/DataCharts/公司概况/工作福利词云.jpg', dpi=100)
    plt.show()
def position_type(get_all_data):
    position_type = open('position_type.txt','w',encoding = 'utf-8')
    get_all_data = list(get_all_data['position'])
    for i in range(len(get_all_data)):
        position_type.write(get_all_data[i])
    position_type.close()
    
    get_text = open('position_type.txt','r',encoding = 'utf-8')
    cut_text = " ".join(get_text)
    wordcloud = WordCloud(font_path = "C:/Windows/Fonts/STKAITI.TTF",
                          background_color = 'white',
                          width = 1000,
                          height = 800)
    wordcloud = wordcloud.generate(cut_text)
    plt.imshow(wordcloud,interpolation = 'bilinear')
    plt.axis('off')
    plt.savefig('C:/WeSite/DataCharts/岗位概况/职位类型词云.jpg', dpi=100)
    plt.show()
