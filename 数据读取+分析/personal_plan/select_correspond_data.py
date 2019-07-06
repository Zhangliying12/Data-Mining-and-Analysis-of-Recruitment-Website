# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
import position_info as pi
import tool

position_dict = {
    'ai':'人工智能',
    'backend':"后端开发",
    'DBA':'数据库管理员',
    'enterprise_software':'企业软件开发',
    'frontend':'前端',
    'hardware_development':'硬件开发',
    'high_position':'高端职位',
    'mobile_development':'移动开发',
    'operation_maintenance':'运维',
    'project_management':'项目管理',
    'software_test':'软件测试'
}

attr = [
    'position',
    'salary_min',
    'salary_max',
    'experience',
    'degree',
    'work_place',
    'company_name',
    'company_type',
    'company_finance',
    'company_scale',
    'bonus',
    'url'
]


#连接数据库
conn = pymysql.connect(host="localhost",user="root",passwd="root",db="job_info",charset="utf8")

def read_from_db(table_name):
    sql = "select * from " + table_name
    df = pd.read_sql(sql,conn)
    return df

# 合并所有数据库中的数据
df_all = pd.DataFrame()
for k in position_dict.keys():
    df = read_from_db(k)
    df_all = pd.concat([df_all,df])
#conn.close()


"""
数据清洗过程：
1. 去掉重复项
2. 去掉含有空值的项和""的项
3. 去掉异常值
"""
# 对每一类型的职位进行数据清洗：
def clean_data(df):
    # 去掉重复项
    df = df.drop_duplicates(subset=['url'])
    # 去掉含有空值和“”的项
    df = df.dropna()
    for att in attr:
        df = df[~df[att].isin([""])]
    # 去掉work_place值异常的项
    df = df[~df['work_place'].str.contains("{{item.city}}")]
    # 去掉异常值
    df = df[~df['salary_max'].isin([1])]
    # 去掉兼职、实习的记录
    df = df[~df['position'].str.contains("实习")]
    df = df[~df['position'].str.contains("兼职")]
    return df

# 对所有数据进行清洗
#print(len(df_all))
df_all = clean_data(df_all)
#print(len(df_all))


# 获取用户提交的信息
sql = "select * from db_produceplan"
df_user_input = pd.read_sql(sql,conn)
id = len(df_user_input)-1

# 用户提交信息不能为空的字段
degree = df_user_input['degree'].values[id]
experience = df_user_input['experience'].values[id]
expected_place = df_user_input['expected_place'].values[id]
expected_job = df_user_input['expected_job'].values[id]
expected_min_salary = df_user_input['expected_min_salary'].values[id]
expected_company_finance = df_user_input['expected_company_finance'].values[id]
expected_bonus = df_user_input['bonus'].values[id]
expected_bonus = expected_bonus.split(",")
# 用户提交信息可以为空的字段
expected_company_finance = df_user_input['expected_company_finance'].values[id]


# print(degree)
# print(experience)
# print(expected_place)
# print(expected_job)
# print(expected_min_salary)
# print(expected_company_finance)
# print(expected_bonus)

# 提取合适的数据

# 将任职地点规范化为省会城市
place_dict = {}
for a in tool.area:
    if expected_place in a:
        expected_place = a[0]
    place_dict[a[0]] = df_all[df_all['work_place'].isin(a)]
if expected_place != '不限':
    df_all = place_dict[expected_place]

if expected_company_finance != '不做要求':
    df_all = df_all[df_all['company_finance'] == expected_company_finance]

if degree != '不限':
    df_all = df_all[df_all['degree'] == degree]

df_all = df_all[df_all['salary_min'] >= expected_min_salary]

# 包含职位关键词的职位全部提取到df_all
df_new = pd.DataFrame()
for key,value in pi.position_keywords.items():
    if key == expected_job:
        for v in value:
            df_new = pd.concat([df_new,df_all[df_all['position'].str.contains(v)]])
df_all = df_new

if experience != '不限':
    df_all = df_all[df_all['experience'] == experience]

import analyse
analyse.analyse_data(df_all,
                     degree,
                     experience,
                     expected_place,
                     expected_job,
                     expected_min_salary,
                     expected_company_finance,
                     expected_bonus,
                     id)