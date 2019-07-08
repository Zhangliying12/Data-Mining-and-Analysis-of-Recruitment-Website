# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:22:16 2019

@author: DELL-1
"""
import data_after_process

import cityposition_number
import shixi
import experience_command
import degree_command
import city_condition
import positiontype_salarymean_and_number

import company_type
import hotcompany_position
import scale
import finance
import word_cloud


import degree_salary
import experience_salary
import finance_salary
import company_scale_salary
import city_salary

#获得清洗后的数据
get_all_data = data_after_process.data_after_process_()


'''
    岗位需求分析
'''


#词云
word_cloud.cloud_company_type(get_all_data)
word_cloud.cloud_company_bonus(get_all_data)
#岗位种类-词云
word_cloud.position_type(get_all_data)

#岗位种类-数量关系
positiontype_salarymean_and_number.mean_and_number(2)

#岗位数量-地区关系
cityposition_number.cityposition_number(get_all_data)

#实习占比-饼状图
shixi.shixi(get_all_data)

#经验需求--饼状图
experience_command.experience_command(get_all_data)

#学位需求--饼状图
degree_command.degree_command(get_all_data)

#获得岗位的城市分布图 -- html
city_condition.area_condition(get_all_data)

#岗位种类-平均工资
positiontype_salarymean_and_number.mean_and_number(1)


'''
    公司状况分析
'''
#公司种类-数量关系
company_type.company_type(get_all_data)

#热门公司-岗位数量-柱状图
hotcompany_position.hotcompany_position(get_all_data)

#公司规模--柱状图
scale.company_scale(get_all_data)

#融资情况--饼状图
finance.finance(get_all_data)


'''
    薪资待遇分析
'''
#薪资水平-学历关系-柱状图
degree_salary.degree_salary(get_all_data)

#薪资水平-经验关系-柱状图
experience_salary.experience_salary(get_all_data)

#薪资水平-融资情况-柱状图
finance_salary.finance_salary(get_all_data)

#薪资水平-公司规模-柱状图
company_scale_salary.company_scale_salary(get_all_data)

#地区和平均薪资-柱状图
city_salary.city_salary(get_all_data)


#positiontype_salarymean_and_number.mean_and_number(2)

#cityposition_number.cityposition_number(get_all_data)

#shixi.shixi(get_all_data)

#experience_command.experience_command(get_all_data)

#degree_command.degree_command(get_all_data)

#city_condition.area_condition(get_all_data)

#positiontype_salarymean_and_number.mean_and_number(1)

#word_cloud.position_type(get_all_data)

#company_type.company_type(get_all_data)

#hotcompany_position.hotcompany_position(get_all_data)

#scale.company_scale(get_all_data)

#finance.finance(get_all_data)

#word_cloud.cloud_company_type(get_all_data)
#word_cloud.cloud_company_bonus(get_all_data)

#degree_salary.degree_salary(get_all_data)

#experience_salary.experience_salary(get_all_data)

#finance_salary.finance_salary(get_all_data)

#company_scale_salary.company_scale_salary(get_all_data)

#city_salary.city_salary(get_all_data)