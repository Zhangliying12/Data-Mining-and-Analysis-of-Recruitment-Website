import pandas as pd
import read_data as rd
import tool

# 合并所有数据库中的数据
df_all = pd.DataFrame()
for k in tool.position_dict.keys():
    df = rd.read_from_db(k)
    df_all = pd.concat([df_all,df])

def clean_data(df):
    # 去掉重复项
    df = df.drop_duplicates(subset=['url'])
    # 去掉含有空值和“”的项
    df = df.dropna()
    for att in tool.attr:
        df = df[~df[att].isin([""])]
    # 去掉work_place值异常的项
    df = df[~df['work_place'].str.contains("{{item.city}}")]
    # 去掉异常值
    df = df[~df['salary_max'].isin([1])]
    return df
df_all = clean_data(df_all)

# 职位数据可视化（实习/ 正式岗位）
df_intership = df_all[df_all['position'].str.contains("实习")]
df_non_intership = df_all[~df_all['position'].str.contains("实习")]
num_intership = len(df_intership)
num_non_intership = len(df_non_intership)
data={}
data['实习'] = num_intership
data['非实习'] = num_non_intership

#画图
colors = ['peachpuff', 'cyan']
tool.drawPie(data_dict=data,
             size = [10,8],
             title="整体数据分布\n实习数据："+str(num_intership)+"\n非实习数据："+str(num_non_intership),
             colors=['peachpuff', 'cyan']
             )
