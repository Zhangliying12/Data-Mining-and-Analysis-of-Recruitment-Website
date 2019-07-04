import matplotlib.pyplot as plt
import collections
# 解决中文无法显示的问题
from pylab import mpl

import read_data as rd
import clean_data as cd
import pandas as pd

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

exp =['经验不限',
    '经验应届毕业生',
    '经验1年以下',
    '经验1-3年',
    '经验3-5年',
    '经验5-10年',
    '经验10年以上']

degree = [
    '不限',
    '大专',
    '本科',
    '硕士',
    '博士'
]

finance = [
    '不需要融资',
    '未融资',
    '天使轮',
    'A轮',
    'B轮',
    'C轮',
    'D轮及以上',
    '上市公司'
]

scale =[
    '少于15人',
    '15-50人',
    '50-150人',
    '150-500人',
    '500-2000人',
    '2000人以上'
]
def read_and_clean_all_data():

    # 合并所有数据库中的数据
    df_all = pd.DataFrame()
    for k in position_dict.keys():
        df = rd.read_from_db(k)
        df_all = pd.concat([df_all, df])

    return cd.clean_data(df_all)

def read_and_clean_by_type():
    # 读取每一类型的职位的数据
    df_ai = cd.clean_data(rd.read_from_db('ai'))
    df_backend = cd.clean_data(rd.read_from_db('backend'))
    df_DBA = cd.clean_data(rd.read_from_db('DBA'))
    df_enterprise_software = cd.clean_data(rd.read_from_db('enterprise_software'))
    df_frontend = cd.clean_data(rd.read_from_db('frontend'))
    df_hardware_development = cd.clean_data(rd.read_from_db('hardware_development'))
    df_high_position = cd.clean_data(rd.read_from_db('high_position'))
    df_mobile_development = cd.clean_data(rd.read_from_db('mobile_development'))
    df_operation_maintenance = cd.clean_data(rd.read_from_db('operation_maintenance'))
    df_project_management = cd.clean_data(rd.read_from_db('project_management'))
    df_software_test = cd.clean_data(rd.read_from_db('software_test'))
    return [df_ai,df_backend,df_DBA,df_enterprise_software,df_frontend,df_hardware_development,df_high_position,df_mobile_development,df_operation_maintenance,df_project_management,df_software_test]

def drawPie(attr_name,value_list,size,title,colors):

    mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

    df_all = read_and_clean_all_data()

    data_dict = collections.Counter(df_all[attr_name])
    data_dict_ord = collections.OrderedDict()

    for e in value_list:
        data_dict_ord[e] = data_dict[e]

    plt.figure(figsize=size)
    sizes = data_dict_ord.values()
    labels = data_dict_ord.keys()
    patches,text1,text2 = plt.pie(sizes,
                          labels=labels,
                          colors=colors,
                          labeldistance = 1.1,#图例距圆心半径倍距离
                          autopct = '%3.2f%%', #数值保留固定小数位
                          shadow = False, #无阴影设置
                          startangle =90, #逆时针起始角度设置
                          pctdistance = 0.6) #数值距圆心半径倍数距离

    plt.axis('equal')
    # 设置图例标题文字大小
    plt.rcParams.update({'font.size': 15})
    plt.legend(title=title,
               loc=1,
               prop={'family':'SimHei','size':15})

    #保存图片
    #plt.savefig("./image/300dpi/整体数据分布饼状图-300dpi.jpg",dpi=300,bbox_inches = 'tight')
    #plt.savefig("./image/200dpi/整体数据分布饼状图-200dpi.jpg",dpi=200,bbox_inches = 'tight')
    #plt.savefig("./image/100dpi/整体数据分布饼状图-100dpi.jpg",dpi=100,bbox_inches = 'tight')
    plt.show()

def drawBar(attr_name,size,num,angle,title,xlabel,ylabel,dir_name):

    mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

    df_all = read_and_clean_all_data()
    data_dict = collections.Counter(df_all[attr_name])
    data_dict = dict(sorted(data_dict.items(), key=lambda d: d[1], reverse=True)[:num])

    plt.figure(figsize=size)
    plt.bar(data_dict.keys(), data_dict.values())
    plt.title(title)
    plt.xlabel(xlabel)
    plt.xticks(rotation=angle)
    plt.ylabel(ylabel)
    plt.savefig("./"+title+".jpg", dpi=300, bbox_inches='tight')
    #plt.savefig("./image/200dpi/不同职位需求柱状图-200dpi.jpg", dpi=200, bbox_inches='tight')
    #plt.savefig("./image/100dpi/不同职位需求柱状图-100dpi.jpg", dpi=100, bbox_inches='tight')
    plt.show()

def drawWordCloud(attr_name):
    from wordcloud import WordCloud, ImageColorGenerator
    import jieba
    df = read_and_clean_all_data()
    text = ''
    for line in df[attr_name]:
        text += ' '.join(jieba.cut(line, cut_all=False))
    backgroud_Image = plt.imread('bonus.jpg')

    wc = WordCloud(
        scale=4,
        background_color='white',
        mask=backgroud_Image,
        font_path='C:\Windows\Fonts\STZHONGS.TTF',
        max_words=2000,
        max_font_size=150,
        random_state=30,
    )
    wc.generate_from_text(text)
    img_colors = ImageColorGenerator(backgroud_Image)
    wc.recolor(color_func=img_colors)
    plt.imshow(wc)
    plt.axis('off')
    #wc.to_file("./image/公司类型词云1.jpg")
    plt.show()
    print('生成词云成功!')


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

area = [hunan,
        hebei,
        jiangxi,
        hainan,
        tianjin,
        hubei,
        shandong,
        heilongjiang,
        neimenggu,
        xizang,
        sichuan,
        jiangsu,
        gansu,
        ningxia,
        xinjiang,
        beijing,
        shanghai,
        guangdong,
        shanxi,
        liaoning,
        henan,
        jilin,
        zhejiang,
        fujian,
        guizhou,
        qinghai,
        guangxi,
        yunnan,
        anhui,
        xianggang,
        aomen,
        chongqing,
        shan_xi
        ]