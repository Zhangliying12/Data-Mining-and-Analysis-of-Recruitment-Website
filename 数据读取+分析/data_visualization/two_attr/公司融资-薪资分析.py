import tool
import matplotlib.pyplot as plt
df_all = tool.read_and_clean_all_data()

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
"""

融资情况与薪资分析可视化

"""
finance_dict = {}

for f in tool.finance:
    df = df_all[df_all['company_finance']==f]
    finance_dict[f] = ((df['salary_min'] + df['salary_max']) / 2).mean()

plt.figure(figsize=[10,5])
plt.bar(finance_dict.keys(),finance_dict.values())
plt.xlabel("公司融资情况")
plt.ylabel("薪资平均水平（单位：K）")
plt.title("融资情况-薪资")

#保存图片
#plt.savefig("./image/300dpi/融资情况与薪资水平-300dpi.jpg",dpi=300,bbox_inches = 'tight')
#plt.savefig("./image/200dpi/融资情况与薪资水平-200dpi.jpg",dpi=200,bbox_inches = 'tight')
#plt.savefig("./image/100dpi/融资情况与薪资水平-100dpi.jpg",dpi=100,bbox_inches = 'tight')
plt.show()