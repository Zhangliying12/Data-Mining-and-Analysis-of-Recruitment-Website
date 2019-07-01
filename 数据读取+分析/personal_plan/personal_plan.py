# -*- coding: utf-8 -*-
import pandas as pd
import MySQLdb

duty_dict={'图像工程师':
'岗位职责：\n1.负责机器学习及图形图像等相关场景的研发工作；\n2.负责数据采集、清洗、汇总、集成等数据相关的流程工作；\n3.负责对公司平台的数据进行整理、挖掘及分析工作；\n4.基于现有产品实现，提出可扩展，高性能，高可用性设计方案；'+
'\n任职资格：\n1.熟悉python、java、shell语言编程(熟悉c/c++属于加分项)；\n2.熟悉Hadoop、Spark大数据处理工具和技术，有两年以上的实际大数据处理经验；\n3.熟悉计算机视觉、图片识别、图像分类、目标检测、图像分割、图片解析等相关技术；\n4.对常用机器学习算法，对CNN、RNN、Fast-rcnn等深度学习算法有了解，对成熟的模型，例如：VGG、AlexNet等有了解；\n5.能够独立完成模型的构建与训练,对深度学习框架tensorflow、keras、Caffe有了解；\n6.对开源的图片处理库opencv、libpng、scikit-image等有了解\n7.责任心强，工作踏实，团队协作精神',

'算法工程师':
'工作职责：为内容消费类产品，提供算法支持，包括:1. 分布式机器学习推荐算法的开发和调优2. 针对大规模数据，进行数据清洗，特征挖掘和统计分析3. 针对信息流推荐、主题推荐等不同应用场景的特定推荐算法开发及调优4. 用户兴趣模型的开发和调优任职要求：1. 熟练使用常用机器学习算法，有1年以上相关项目开发经验。熟悉深度学习算法者优先2. 有信息流、个性化推荐、情感分析等算法项目经验者优先3. 熟练使用hadoop或spark计算平台，具有1年以上大规模数据并行计算经验4. 精通至少一门编程语言，熟练使用scala、java者优先5. 熟练使用至少一种机器学习算法工具包，熟练使用mllib者优先6. 熟练使用hive和mys7. 工作态度认真积极，目标导向型优先',

'机器学习算法工程师':
'工作职责:1.能够使用机器学习算法有效的挖掘海量数据并从中发现规律或者建立模型提供商业决策2.对业务数据，用户数据，行为数据进行深度挖掘分析，发现数据背后的规律，完成对用户画像，营销以及风险控制的建模3.利用数据挖掘，机器学习，以及自然语言处理等相关算法，解决业务需求，提高产品用户体验，提升转换率4.负责机器学习建模和效果优化，负责个性化推荐算法设计和效果优化任职资格:1.硕士以上学历，计算机、大数据、金融、经济学相关等专业2.3年以上算法分析相关经验，熟练使用SQL、R、Python等进行数据分析、数据挖掘3.熟悉机器学习常用算法，有搜索、广告、推荐系统经验者优先4.优秀的分析问题和解决问题能力，对解决挑战性的问题充满激情5.熟悉Hadoop/HBase/Hive/Storm/Spark/Kafka分布式大数据处理系统者优先',

'深度学习算法工程师':
'岗位职责：1、从事深度学习领域的算法模型研究工作，2、负责视频、图像相关项目深度学习模型的开发和部署。3、负责单位深度学习模型成果沉淀和产品转化。岗位要求：1、研究生以上学历，有良好的数学基础；2、从事过深度学习视觉方面的研究或有深度学习视觉项目相关经验；3、熟悉深度学习算法，特别是CNN和RNN；4、能熟练运用 tensorflow、PyTorch、Keras、Caffe 其中一种框架进行深度学习模型训练和开发；5、具有良好的团队合作精神。',
'视觉设计师':
'岗位职责1. 负责政务类移动端业务体验设计支持，及运营推广相关设计。2. 参与设计体验、流程的制定和规范；3. 参与整个设计过程中的评审，负责视觉实现的检查，监督产品视觉的实现质量；4. 关注用户反馈与沟通，根据分析结果持续优化设计；5. 参与分享设计经验，提高团队的设计能力。岗位要求1. 从事设计行业工作 3 年以上2. 热爱设计，拥有宽广的行业（平?面设计、互联网、手持应用）视野与时尚的审美标准3. 对网站设计有丰富经验，有成功案例（有桌面、移动端多平台案例者更佳）4. 有丰富的设计理论知识和对流行趋势敏锐的洞察力，推动改善提升团队的设计能力5. 对用户研究有一定经验和见解6. 善于沟通，具备良好合作态度团队精神，富有工作激情、创造力和责任感，有不断学习的良好习惯，能承受高强度的工作压力7. 美术、设计或相关专业本科以上学历，手绘原创能力较强或具备一定交互设计能力可优先考虑',

'NLP算法工程师':
'岗位职责:1. 运用前沿深度学习和机器学习相关技术优化机器翻译、语义理解等模型2. 机器翻译引擎的设计及研发3. 句法分析、语义分析等自然语言处理相关算法的研发4. 对应用部门提出的引擎性能需求提供解决方案，进行效果调优岗位要求:1. 计算机相关专业毕业，硕士以上学历优先，英语或日语良好2. 熟悉自然语言处理，机器学习，深度学习等常用算法，能够跟踪NLP领域的最新研究方向3. 有相关工作经历或实验室背景，包括但不限于以下方向：机器翻译、智能对话、知识图谱等4. 熟悉Linux开发环境，较强的C/C++编程和算法基础，熟练使用Python、shell等脚本语言5.良好的团队合作精神，较强的沟通能力'}

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
conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="job_info",charset="utf8")

def read_from_db(table_name):
    sql = "select * from " + table_name
    df = pd.read_sql(sql,conn)
    return df

# 读取每一类型的职位的数据
df_ai = read_from_db('ai')
df_backend = read_from_db('backend')
df_DBA = read_from_db('DBA')
df_enterprise_software = read_from_db('enterprise_software')
df_frontend = read_from_db('frontend')
df_hardware_development = read_from_db('hardware_development')
df_high_position = read_from_db('high_position')
df_mobile_development = read_from_db('mobile_development')
df_operation_maintenance = read_from_db('operation_maintenance')
df_project_management = read_from_db('project_management')
df_software_test = read_from_db('software_test')

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

# 分职位对数据进行清洗
df_ai = clean_data(df_ai)
df_backend = clean_data(df_backend)
df_DBA = clean_data(df_DBA)
df_enterprise_software = clean_data(df_enterprise_software)
df_frontend = clean_data(df_frontend)
df_hardware_development = clean_data(df_hardware_development)
df_high_position = clean_data(df_high_position)
df_mobile_development = clean_data(df_mobile_development)
df_operation_maintenance = clean_data(df_operation_maintenance)
df_project_management = clean_data(df_project_management)
df_software_test = clean_data(df_software_test)

# 对所有数据进行清洗
print(len(df_all))
df_all = clean_data(df_all)
print(len(df_all))

sql = "select * from table_produceplan"
df_info = pd.read_sql(sql,conn)
id = len(df_info)-1

# 不能为空的字段
degree = df_info['degree'].values[id]
experience = df_info['experience'].values[id]

# 可以为空的字段
position = df_info['expected_job'].values[id]
company_name = df_info['expected_company_name'].values[id]
salary_min = df_info['expected_min_salary'].values[id]
place = df_info['expected_place'].values[id]

def isNone(attr):
    return attr is None

df_all = df_all[df_all['degree']==degree]
df_all = df_all[df_all['experience']==experience]

if position and company_name and salary_min and place:



#df_all = df_all[df_all['position']==position]
#df_all = df_all[df_all['company_name']==company_name]
#df_all = df_all[df_all['salary_min']>=salary_min]
#df_all = df_all[df_all['work_place']==place]

print(degree)
print(experience)
print(position)
print(company_name)
print(salary_min)
print(place)

#print(df_all)

#df_all = df_all[df_all['position']==position]
str_1 = "您好，根据您的选择，我们为您找到合适职位信息"+str(len(df_all))+"条。\n"
str_2 = "您选择的职位有以下职责和要求：\n"
str_3 = duty_dict[position]

file_name = "tips"+str(id)+'.txt'
with open(file_name,'w') as f:
    f.write(str_1+str_2+str_3)


