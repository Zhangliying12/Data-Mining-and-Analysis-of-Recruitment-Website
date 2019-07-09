import tool
import matplotlib.pyplot as plt
df_all = tool.read_and_clean_all_data()

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
"""

公司规模与薪资分析可视化

"""
scale_dict = {}

for s in tool.scale:
    df = df_all[df_all['company_scale']==s]
    scale_dict[s] = ((df['salary_min'] + df['salary_max']) / 2).mean()

plt.figure(figsize=[10,5])
scale_dict = dict(sorted(scale_dict.items(), key=lambda d:d[1], reverse = True))

plt.bar(scale_dict.keys(),scale_dict.values())
plt.title(label='公司规模与薪资水平')
plt.xlabel('公司规模',labelpad=20)
plt.ylabel('薪资平均水平(单位：K)')

#保存图片
#plt.savefig("./image/300dpi/公司规模与薪资水平-300dpi.jpg",dpi=300,bbox_inches = 'tight')
#plt.savefig("./image/200dpi/公司规模与薪资水平-200dpi.jpg",dpi=200,bbox_inches = 'tight')
#plt.savefig("./image/100dpi/公司规模与薪资水平-100dpi.jpg",dpi=100,bbox_inches = 'tight')
plt.show()