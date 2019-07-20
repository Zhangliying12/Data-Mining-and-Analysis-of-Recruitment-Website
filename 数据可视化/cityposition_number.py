# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:14:08 2019

@author: DELL-1
"""

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

def cityposition_number(get_all_data):
    sichuan = ['四川','自贡','攀枝花','泸州','德阳','绵阳','广元',
               '遂宁','内江','眉山','广安','达州','雅安',
               '资阳','成都','乐山','宜宾','南充','巴中',
               '阿坝藏族羌族自治州','甘孜藏族自治州','凉山彝族自治州']
    
    jiangsu = ['江苏','扬州','镇江','宿迁','连云港','徐州','淮安','盐城','泰州','常州','无锡',
               '苏州','南京','南通']
    
    gansu   = ['甘肃','嘉峪关','金昌','白银','武威','酒泉','平凉','庆阳','陇南','天水','定西','兰州',
               '张掖','甘南藏族自治州','临夏回族自治州']
    
    ningxia = ['宁夏','石嘴山','吴忠','固原','中卫','银川']
    
    xinjiang = ['新疆','克拉玛依','吐鲁番','哈密','昌吉回族自治州','和田','阿克苏','喀什',
                '克孜勒苏柯尔克孜自治州','巴音郭楞蒙古自治州','博尔塔拉蒙古自治州',
                '伊犁哈萨克自治州','塔城','阿勒泰','乌鲁木齐']
    
    beijing  = ['北京','延庆','密云','怀柔','昌平','平谷','顺义','海淀','东城',
                '朝阳','西城','门头沟','石景山','丰台','房山','大兴']
    
    shanghai = ['上海','杨浦','黄浦','虹口','闸北','静安','普陀','长宁','徐汇','浦东新',
               '闵行','宝山','嘉定','青浦','松江','奉贤','金山']
    
    guangdong = ['广东','珠海','汕头','韶关','江门','湛江','茂名','肇庆','惠州','河源',
                 '阳江','清远','中山','揭阳','云浮','梅州','潮州','汕尾','东莞','深圳',
                 '佛山','广州']
    
    shanxi = ['山西','忻州','吕梁','运城','大同','朔州','太原','阳泉','晋中','临汾',
              '长治','晋城']
    
    liaoning = ['辽宁','盘锦','铁岭','抚顺','沈阳','辽阳','本溪','阜新','朝阳','锦州',
                '鞍山','营口','丹东','大连','葫芦岛']
    
    henan = ['河南','开封','洛阳','漯河','商丘','三门峡','平顶山','周口','安阳','濮阳',
             '新乡','焦作','郑州','许昌','驻马店','信阳','南阳','鹤壁']
    
    jilin = ['吉林','四平','通化','白山','辽源','松原','白城','长春','延边朝鲜族自治州']
    
    zhejiang = ['浙江','湖州','舟山','嘉兴','杭州','绍兴','宁波','台州','金华','丽水','温州','衢州']
    
    fujian = ['福建','宁德','莆田','南平','福州','三明','泉州','龙岩','厦门','漳州']
    
    guizhou = ['贵州','安顺','毕节','遵义','铜仁','六盘水','贵阳',
               '黔南布依族苗族自治州','黔东南苗族侗族自治州','黔西南苗族布依族自治州']
    
    qinghai = ['青海','玉树','果洛','海东','海西','海南','海北','西宁','黄南']
    
    guangxi = ['广西','北海','防城港','钦州','贵港','百色','贺州','河池','来宾',
               '崇左','桂林','柳州','梧州','玉林','南宁']
    
    yunnan = ['云南','曲靖','玉溪','普洱','保山','丽江','昆明','临沧','昭通',
              '西双版纳','大理','楚雄','红河','文山','德宏','怒江','迪庆']
    
    anhui  = ['安徽','芜湖','马鞍山','淮北','铜陵','黄山','池州','亳州','宿州','蚌埠',
              '淮南','阜阳','滁州','合肥','六安','安庆','宣城','巢湖']
    
    shan_xi = ['陕西','渭南','延安','商洛','榆林','铜川','咸阳','宝鸡','汉中','安康','西安']
    
    chongqing = ['重庆']
    
    hunan = ['湖南','株洲','湘潭','邵阳','岳阳','常德','益阳','娄底','长沙','衡阳','永州',
             '怀化','张家界','郴州','湘西土家族苗族自治州']
    
    hebei = ['河北','承德','秦皇岛','唐山','张家口','廊坊','保定','沧州','衡水',
             '石家庄','邢台','邯郸']
    
    jiangxi=['江西','九江','鹰潭','新余','景德镇','抚州','上饶','南昌','宜春','萍乡',
             '赣州','吉安']
    
    hainan=['海南','海口','三亚','海南岛']
    
    tianjin=['天津','蓟县','静海','宁河','静海','宝坻','武清','滨海',
             '津南','北辰','红桥','河北区','河东','河西','和平','西青',
             '红桥']
    
    hubei=['湖北','黄石','十堰','宜昌','荆门','鄂州','孝感','黄冈','随州','恩施',
           '襄阳','武汉','咸宁','荆州','襄樊']
    
    shandong=['山东','烟台','日照','威海','莱芜','枣庄','菏泽','德州','滨州','东营',
              '潍坊','青岛','聊城','济南','临沂','南岛','淄博','泰安','济宁']
    
    heilongjiang= ['黑龙江','佳木斯','鹤岗','鸡西','双鸭山','黑河','七台河','绥化',
                   '伊春','牡丹江','哈尔滨','大庆','齐齐哈尔','大兴安岭']
    
    neimenggu = ['内蒙古','呼伦贝尔','通辽','乌海','赤峰','乌兰察布','鄂尔多斯',
                 '包头','呼和浩特','巴彦淖尔','锡林郭勒盟','阿拉善盟','兴安盟']
    
    xizang = ['西藏','阿里','那曲','昌都','林芝','山南','日喀则','拉萨']
    
    xianggang = ['香港特别行政区']
    
    aomen = ['澳门特别行政区']
    
    taiwan = ['台湾','高雄','台北']
    
    
    area = [sichuan, jiangsu, gansu, ningxia, xinjiang, beijing, shanghai, guangdong,
            shanxi, liaoning, henan, jilin, zhejiang, fujian, guizhou, qinghai,
            guangxi, yunnan, anhui, shan_xi, chongqing, hunan, hebei, jiangxi,
            hainan, tianjin, hubei, shandong, heilongjiang, neimenggu, xizang,
            xianggang, aomen, taiwan]
    
    #get_all_data = data_after_process.data_after_process_()
    
    cityposition_number = {}
    for i in area:
        area = get_all_data[False^get_all_data['work_place'].isin(i)]
        cityposition_number[i[0]] =len(area['work_place'])
    del cityposition_number['香港特别行政区']
    del cityposition_number['澳门特别行政区']
    del cityposition_number['台湾']

    cityposition_number = dict(sorted(cityposition_number.items(), key=lambda d:d[1], reverse = True))
    attr = cityposition_number.keys()
    value = cityposition_number.values()
    plt.figure(figsize=(10,10))

    plt.bar(attr,
            value,
            edgecolor='black')
    for a,b in zip(attr,value):
        plt.text(a,b+0.3,b,ha='center',va='bottom')

    plt.xlabel("地区", fontsize = 20)
    plt.ylabel("职位数量", fontsize = 20)
    plt.title("地区岗位需求分布", fontsize = 20)
    plt.xticks(rotation = 90, fontsize = 15)
    plt.yticks(fontsize = 20)
    plt.savefig('C:/WeSite/DataCharts/岗位概况/分地区岗位需求分布-100dpi.jpg', dpi=100)
    #plt.show()

