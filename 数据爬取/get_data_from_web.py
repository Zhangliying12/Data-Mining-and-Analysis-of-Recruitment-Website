# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:16:55 2019
@author: DELL-1
"""
import time
import urllib.request
import urllib.error
import re
import pymysql


def proxy_server(url,proxy):
        #模拟浏览器
        url = urllib.request.Request(url)
        url.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134')
        #代理服务器
        proxy = urllib.request.ProxyHandler({'http':proxy})
        opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode()
        return data

        
conn = pymysql.connect(host = '127.0.0.1',
                       user = 'root',
                       passwd = 'root',
                       db = 'job_info')

cursor = conn.cursor()

#数据库表
mysql_keyword = ['ai',
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

#正则表达式
position = 'data-positionname="(.*?)"'
salary_min = 'data-salary="(.*?)k'                           
salary_max = 'data-salary=".*?-(.*?)k"'                         
experience = '<span class="money">.*?<[/]span>\s*<!--<i><[/]i>-->(.*?)\s*[/]'                       
degree = '<span class="money">.*?<[/]span>\s*<!--<i><[/]i>-->.*?\s*[/]\s*(.*)'                
work_place = '<span class="add">[[]<em>(.*)·'
company_name = 'data-company="(.*?)"'                    
company_type = '<div class="industry">\s*(.*?)\s*/'                  
company_finance = '<div class="industry">\s*.*?\s*/\s*(.*?)\s*/'                           
company_scale = '<div class="industry">\s*.*?\s*/\s*.*?\s*/\s*(.*?)\s*</div>'                    
bonus = '</div>\s*<div class="li_b_r">“(.*?)”'                                             
url = '<a class="position_link" href="(.*?)"'

proxy = '163.204.242.227:9999'

keyword = ['Java','C%2B%2B','PHP','shujuwajue','sousuosuanfa','jingzhuntuijian',
           'C'   ,'C%23'   ,'quanzhangongchengshi','.NET','Hadoop','Python',
           'Delphi','VB','Perl','Ruby','Node.js','go','asp','shell','qukuailian',
           'houduankaifaqita',
           
           'HTML5','Android','iOS','WP','yidongkaifaqita',
         
           'webqianduan','Flash','html51','JavaScript','U3D','COCOS2D-X',
           'qianduankaifaqita',
            
           'shenduxuexi','jiqixuexi','tuxiangchuli','tuxiangshibie','yuyinshibie',
           'jiqishijue','suanfagongchengshi','ziranyuyanchuli',
            
           'ceshigongchengshi','zidonghuaceshi','gongnengceshi','xingnengceshi',
           'ceshikaifa','youxiceshi','baiheceshi','huiheceshi','heiheceshi',
           'shoujiceshi','yingjianceshi','ceshijingli2','ceshiqita',
            
           'yunweigongchengshi','yunweikaifagongchengshi','wangluogongchengshi',
           'xitonggongchengshi','ITzhichi','idc','cdn','f5','xitongguanliyuan',
           'bingdufenxi','webanquan','wangluoanquan','xitonganquan','yunweijingli',
           'yunweiqita',
           
           'MySQL','SQLServer','Oracle','DB2','MongoDB','etl','hive','shujucangku',
           'dbaqita',
           
           'jishujingli','jishuzongjian','jiagoushi','CTO','yunweizongjian',
           'jishuhehuoren','xiangmuzongjian','ceshizongjian','anquanzhuanjia',
           'gaoduanjishuzhiweiqita',
           
           'yingjian','qianrushi','zidonghua','danpianji','dianlusheji',
           'qudongkaifa','xitongjicheng','fpgakaifa','dspkaifa','armkaifa',
           'pcbgongyi','mujusheji','rechuandao','cailiaogongchengshi',
           'jingyigongchengshi','shepingongchengshi','yingjiankaifaqita', 
           
           'xiangmujingli','xiangmuzhuli',
           
           'shishigongchengshi','shouqiangongchengshi','shouhougongchengshi',
           'bigongchengshi','qiyeruanjianqita'                          
           ]

print(len(keyword))

for i in range(len(keyword)):
    if i <= 21:
        sql = "insert into backend(position,salary_min,salary_max,experience,degree,work_place,company_name,company_type,company_finance,company_scale,bonus,url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    elif i > 21 and i <= 26:
        sql = "insert into mobile_development(position,salary_min,salary_max,experience,degree,work_place,company_name,company_type,company_finance,company_scale,bonus,url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    elif i > 26 and i <= 33:
        sql = "insert into frontend(position,salary_min,salary_max,experience,degree,work_place,company_name,company_type,company_finance,company_scale,bonus,url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    elif i > 33 and i <= 41:
        sql = "insert into ai(position,salary_min,salary_max,experience,degree,work_place,company_name,company_type,company_finance,company_scale,bonus,url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    elif i > 41 and i <= 54:
        sql = "insert into software_test(position,salary_min,salary_max,experience,degree,work_place,company_name,company_type,company_finance,company_scale,bonus,url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    elif i > 54 and i <= 69:
        sql = "insert into operation_maintenance(position,salary_min,salary_max,experience,degree,work_place,company_name,company_type,company_finance,company_scale,bonus,url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    elif i > 69 and i <= 78:
        sql = "insert into dba(position,salary_min,salary_max,experience,degree,work_place,company_name,company_type,company_finance,company_scale,bonus,url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    elif i > 78 and i <= 88:
        sql = "insert into high_position(position,salary_min,salary_max,experience,degree,work_place,company_name,company_type,company_finance,company_scale,bonus,url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    elif i > 88 and i <= 90:
        sql = "insert into project_management(position,salary_min,salary_max,experience,degree,work_place,company_name,company_type,company_finance,company_scale,bonus,url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    elif i > 90 and i <= 107:
        sql = "insert into hardware_development(position,salary_min,salary_max,experience,degree,work_place,company_name,company_type,company_finance,company_scale,bonus,url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    elif i > 107 and i <= 112:
        sql = "insert into enterprise_software(position,salary_min,salary_max,experience,degree,work_place,company_name,company_type,company_finance,company_scale,bonus,url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    else:
        break   
    for j in range(1,3):
        try:
            httpurl = 'https://www.lagou.com/zhaopin/'+keyword[i]+'/'+str(j)+'/?filterOption=3'
            data = proxy_server(httpurl,proxy)

            position_result = re.findall(position,data)
            salary_min_result = re.findall(salary_min,data)
            salary_max_result = re.findall(salary_max,data)
            experience_result = re.findall(experience,data)
            degree_result = re.findall(degree,data)
            work_place_result = re.findall(work_place,data)
            company_name_result = re.findall(company_name,data)
            company_type_result = re.findall(company_type,data)
            company_finance_result = re.findall(company_finance,data)
            company_scale_result = re.findall(company_scale,data)
            bonus_result = re.findall(bonus,data)
            url_result = re.findall(url,data)

            for k in range(len(bonus_result)):
                time.sleep(2)
                cursor.execute(sql,
                               [position_result[k],
                                int(salary_min_result[k]),
                                int(salary_max_result[k]),
                                experience_result[k],
                                degree_result[k],
                                work_place_result[k],
                                company_name_result[k],
                                company_type_result[k],
                                company_finance_result[k],
                                company_scale_result[k],
                                bonus_result[k],
                                url_result[k]])
                print(keyword[i]+str(j)+'页,第'+str(k)+'条数据成功')
                conn.commit()
        except urllib.error.URLError as e:
            if hasattr(e,'code'):
                print(e.code)
            if hasattr(e,'reason'):
                print(e.reason)
            print(keyword[i]+str(j)+'页,第'+str(k)+'条数据成功')
            continue
        except Exception as e:
            print('Exception:'+str(e))
            print(keyword[i]+str(j)+'页,第'+str(k)+'条数据成功')
            continue

cursor.close()

conn.close()