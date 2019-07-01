import matplotlib.pyplot as plt
import numpy as np
import tool
"""
按职位进行平均工资分析
"""
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

#del salary_avg_by_position['高端职位']
df_list = tool.read_and_clean_by_type()

data_dict = {}
i = 0
for k in tool.position_dict.values():
    data_dict[k] = df_list[i]
    i = i + 1

salary_avg_by_position = {}
for name, data in data_dict.items():
    salary_avg_by_position[name] = ((data['salary_min'] + data['salary_max']) / 2).mean()

salary_avg_by_position = dict(sorted(salary_avg_by_position.items(), key=lambda d:d[1], reverse = False))
group_data = list(salary_avg_by_position.values())
group_names = list(salary_avg_by_position.keys())
group_mean = np.mean(group_data)

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.barh(group_names, group_data)

ax.axvline(group_mean, ls='--', color='r')
ax.set(xlim=[0,40], xlabel='薪资（单位：K）', ylabel='职位类型',title='平均工资分析')

#plt.savefig("./image/300dpi/按职位类型平均工资分析柱状图-300dpi.jpg",dpi=300,bbox_inches = 'tight')
#plt.savefig("./image/200dpi/按职位类型平均工资分析柱状图-200dpi.jpg",dpi=200,bbox_inches = 'tight')
#plt.savefig("./image/100dpi/按职位类型平均工资分析柱状图-100dpi.jpg",dpi=100,bbox_inches = 'tight')
plt.show()