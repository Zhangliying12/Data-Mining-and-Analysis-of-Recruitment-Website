# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:31:05 2019
@author: DELL-1
"""
import pymysql
import pandas as pd
import data_after_process
import matplotlib
import matplotlib.pyplot as plt

#支持中文
matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False


def mean_and_number(key):
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           passwd = 'root',
                           db = 'job_info')
    #数据库表
    keyword = ['ai',
               'backend',
               'dba',
               'enterprise_software',
               'frontend',
               'hardware_development',
               'high_position',
               'mobile_development',
               'operation_maintenance',
               'project_management',
               'software_test']
    
    
    #数据提取表达式
    select_ai = "select * from "+keyword[0]
    select_backend = "select * from "+keyword[1]
    select_dba = "select * from "+keyword[2]
    select_enterprise_software = "select * from "+keyword[3]
    select_hardware_development = "select * from "+keyword[4]
    select_high_position = "select * from "+keyword[5]
    select_mobile_development = "select * from "+keyword[6]
    select_operation_maintenance = "select * from "+keyword[7]
    select_project_management = "select * from "+keyword[8]
    select_software_test = "select * from "+keyword[9]
    select_frontend = "select * from "+keyword[10]
    
        
    #数据提取
    get_ai = pd.read_sql(select_ai,conn)
    get_backend = pd.read_sql(select_backend,conn)
    get_dba = pd.read_sql(select_dba,conn)
    get_enterprise_software = pd.read_sql(select_enterprise_software,conn)
    get_hardware_development = pd.read_sql(select_hardware_development,conn)
    get_high_position = pd.read_sql(select_high_position,conn)
    get_mobile_development = pd.read_sql(select_mobile_development,conn)
    get_operation_maintenance = pd.read_sql(select_operation_maintenance,conn)
    get_project_management = pd.read_sql(select_project_management,conn)
    get_software_test = pd.read_sql(select_software_test,conn)
    get_frontend = pd.read_sql(select_frontend,conn)
    
    conn.close()
    get_ai = data_after_process.one_table_process(get_ai)
    get_backend = data_after_process.one_table_process(get_backend)
    get_dba = data_after_process.one_table_process(get_dba)
    get_enterprise_software = data_after_process.one_table_process(get_enterprise_software)
    get_hardware_development = data_after_process.one_table_process(get_hardware_development)
    get_high_position = data_after_process.one_table_process(get_high_position)
    get_mobile_development = data_after_process.one_table_process(get_mobile_development)
    get_operation_maintenance = data_after_process.one_table_process(get_operation_maintenance)
    get_project_management = data_after_process.one_table_process(get_project_management)
    get_software_test = data_after_process.one_table_process(get_software_test)
    get_frontend = data_after_process.one_table_process(get_frontend)
    
    keyword = ['人工智能','后端开发','DBA','企业软件','硬件开发',
               '高端职位','移动开发','运维','项目管理','软件测试','前端开发']
    if key == 1:
        ai_salary = ((get_ai['salary_min'] + get_ai['salary_max'])/2).mean()
        backend_salary = ((get_backend['salary_min'] + get_backend['salary_max'])/2).mean()
        dba_salary = ((get_dba['salary_min'] + get_dba['salary_max'])/2).mean()
        enterprise_software_salary = ((get_enterprise_software['salary_min'] + get_enterprise_software['salary_max'])/2).mean()
        hardware_development_salary = ((get_hardware_development['salary_min'] + get_hardware_development['salary_max'])/2).mean()
        high_position_salary = ((get_high_position['salary_min'] + get_high_position['salary_max'])/2).mean()
        mobile_development_salary = ((get_mobile_development['salary_min'] + get_mobile_development['salary_max'])/2).mean()
        operation_maintenance_salary = ((get_operation_maintenance['salary_min'] + get_operation_maintenance['salary_max'])/2).mean()
        project_management_salary = ((get_project_management['salary_min'] + get_project_management['salary_max'])/2).mean()
        software_test_salary = ((get_software_test['salary_min'] + get_software_test['salary_max'])/2).mean()
        frontend_salary = ((get_frontend['salary_min'] + get_frontend['salary_max'])/2).mean()
        
        mean_salary = [ai_salary,
                       backend_salary,
                       dba_salary,
                       enterprise_software_salary,
                       hardware_development_salary,
                       high_position_salary,
                       mobile_development_salary,
                       operation_maintenance_salary,
                       project_management_salary,
                       software_test_salary,
                       frontend_salary]

        position_salary_dict = dict(zip(keyword,mean_salary))
        #print(position_salary_dict.keys())
        position_salary_dict = dict(sorted(position_salary_dict.items(),key=lambda d:d[1],reverse=False))
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
                 '#7171C6',
                 '#698B22']
        print("职位-薪资")
        print(list(position_salary_dict.keys()))
        print(list(position_salary_dict.values()))
        plt.barh(list(position_salary_dict.keys()),
                 list(position_salary_dict.values()),
                 color = color,
                 edgecolor = 'black')
        for a,b in zip(keyword,mean_salary):
            plt.text(b+1,a,'%.2f'%b,ha='center',va='bottom',fontsize=15)

        plt.xlabel("平均薪资（单位：千元）",fontsize=20)
        plt.ylabel("职位类别",fontsize=20)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.title("职位类别与平均薪资关系",fontsize=20)
        plt.savefig('C:/WeSite/DataCharts/岗位概况/薪资概况/按职位类型平均工资分析柱状图-100dpi.jpg', dpi=100)
        #plt.show()

    elif key==2:      
        type_ai = len(get_ai)
        type_backend = len(get_backend)
        type_dba =len(get_dba)
        type_enterprise_software = len(get_enterprise_software)
        type_hardware_development = len(get_hardware_development)
        type_high_position = len(get_high_position)
        type_mobile_development = len(get_mobile_development)
        type_operation_maintenance = len(get_operation_maintenance)
        type_project_management = len(get_project_management)
        type_software_test = len(get_software_test)
        type_frontend = len(get_frontend)
           
        positiontype = [type_ai,
                        type_backend,
                        type_dba,
                        type_enterprise_software,
                        type_hardware_development,
                        type_high_position,
                        type_mobile_development,
                        type_operation_maintenance,
                        type_project_management,
                        type_software_test,
                        type_frontend]
        plt.figure(figsize=(13,13))
        position_num_dict = dict(zip(keyword,positiontype))
        position_num_dict = dict(sorted(position_num_dict.items(),key=lambda d:d[1],reverse=False))
        print("职位-数量")
        print(list(position_num_dict.keys()))
        print(list(position_num_dict.values()))
        color = ['red',
                 'orange',
                 'yellow',
                 'green',
                 '#48D1CC',
                 'blue',
                 'purple',
                 '#4A4A4A',
                 '#A52A2A',
                 '#7171C6',
                 '#698B22'] 
        plt.barh(list(position_num_dict.keys()),
                 list(position_num_dict.values()),
                 color = color,
                 edgecolor = '#0000AA')
        for a,b in zip(keyword,positiontype):
            plt.text(b+0.8,a,b,ha='center',va='bottom',fontsize=20)
        plt.xlabel("岗位数量",fontsize=20)
        plt.xticks(fontsize=20)
        plt.ylabel("岗位类型",fontsize=20)
        plt.yticks(fontsize=20)
        plt.title("岗位类型-数量需求",fontsize=20)
        plt.savefig('C:/WeSite/DataCharts/岗位概况/不同职位需求柱状图-100dpi.jpg', dpi=100)
        #plt.show()

    else:
        return 0
