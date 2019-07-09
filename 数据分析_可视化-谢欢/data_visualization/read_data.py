import MySQLdb
import pandas as pd

def read_from_db(table_name):
    # 连接数据库
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="job_info", charset="utf8")
    sql = "select * from " + table_name
    df = pd.read_sql(sql,conn)
    return df
