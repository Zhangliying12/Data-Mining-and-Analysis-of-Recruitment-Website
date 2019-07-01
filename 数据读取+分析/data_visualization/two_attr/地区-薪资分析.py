import tool
import matplotlib.pyplot as plt
df_all = tool.read_and_clean_all_data()

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

place_salary ={}
for a in tool.area:
    df = df_all[df_all['work_place'].isin(a)]
    place_salary[a[0]]=((df['salary_min']+df['salary_max'])/2).mean()

# 绘制地区-薪资关系柱状图
place_salary = dict(sorted(place_salary.items(), key=lambda d:d[1], reverse = True))
del place_salary['香港特别行政区']
del place_salary['澳门特别行政区']
plt.figure(figsize=(20,9))
plt.bar(place_salary.keys(), place_salary.values())
plt.title('地区-薪资分析')
plt.xlabel('地区')
plt.ylabel('薪资（单位：K）')
#plt.savefig("./image/300dpi/地区-薪资分析-300dpi.jpg",dpi=300,bbox_inches = 'tight')
#plt.savefig("./image/200dpi/地区-薪资分析-200dpi.jpg",dpi=200,bbox_inches = 'tight')
#plt.savefig("./image/100dpi/地区-薪资分析-100dpi.jpg",dpi=100,bbox_inches = 'tight')
plt.show()