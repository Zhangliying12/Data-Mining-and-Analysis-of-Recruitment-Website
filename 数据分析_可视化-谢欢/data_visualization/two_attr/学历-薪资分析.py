import tool
import matplotlib.pyplot as plt
df_all = tool.read_and_clean_all_data()

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
"""

学历要求与薪资分析可视化

"""
degree_dict = {}

for d in tool.degree:
    df = df_all[df_all['degree'] == d]
    degree_dict[d] = ((df['salary_min'] + df['salary_max']) / 2).mean()

# print(degree_dict)

plt.bar(degree_dict.keys(), degree_dict.values())
plt.xlabel("学历")
plt.ylabel("薪资平均水平（单位：K）")
plt.title("学历-薪资")

# 保存图片
#plt.savefig("./image/300dpi/学历与薪资水平-300dpi.jpg", dpi=300, bbox_inches='tight')
#plt.savefig("./image/200dpi/学历与薪资水平-200dpi.jpg", dpi=200, bbox_inches='tight')
#plt.savefig("./image/100dpi/学历与薪资水平-100dpi.jpg", dpi=100, bbox_inches='tight')
plt.show()