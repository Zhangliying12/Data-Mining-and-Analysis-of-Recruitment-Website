import tool
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
    for att in tool.attr:
        df = df[~df[att].isin([""])]
    # 去掉work_place值异常的项
    df = df[~df['work_place'].str.contains("{{item.city}}")]
    # 去掉异常值
    df = df[~df['salary_max'].isin([1])]
    # 去掉兼职、实习的记录
    df = df[~df['position'].str.contains("实习")]
    df = df[~df['position'].str.contains("兼职")]
    return df