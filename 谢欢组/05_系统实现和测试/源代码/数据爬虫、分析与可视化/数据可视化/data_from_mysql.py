# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 11:00:42 2019

@author: DELL-1
"""
import pymysql
import pandas as pd

def get_data_from_mysql():
    conn = pymysql.connect(host = '127.0.0.1',
                           user = 'root',
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
    
    #数据合并
    get_data_all = [get_ai,
                    get_backend,
                    get_dba,
                    get_enterprise_software,
                    get_hardware_development,
                    get_high_position,
                    get_mobile_development,
                    get_operation_maintenance,
                    get_project_management,
                    get_software_test,
                    get_frontend
                    ]
    get_data_all = pd.concat(get_data_all)
    conn.close()
    return get_data_all