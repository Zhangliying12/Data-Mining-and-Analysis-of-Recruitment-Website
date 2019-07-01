import tool
import matplotlib.pyplot as plt
df_all = tool.read_and_clean_all_data()

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

work_place_dict ={}
for a in tool.area:
    df = df_all[df_all['work_place'].isin(a)]
    work_place_dict[a[0]] = len(df)


# 分地区岗位需求分布

work_place_dict= dict(sorted(work_place_dict.items(), key=lambda d:d[1], reverse = True))
del work_place_dict['香港特别行政区']
del work_place_dict['澳门特别行政区']
plt.figure(figsize=(20,9))
plt.bar(work_place_dict.keys(), work_place_dict.values())
plt.title('分地区岗位需求')
plt.xlabel('地区')
plt.ylabel('岗位数量(单位：个)')
#plt.savefig("./image/300dpi/分地区岗位需求分布-300dpi.jpg",dpi=300,bbox_inches = 'tight')
#plt.savefig("./image/200dpi/分地区岗位需求分布-200dpi.jpg",dpi=200,bbox_inches = 'tight')
#plt.savefig("./image/100dpi/分地区岗位需求分布-100dpi.jpg",dpi=100,bbox_inches = 'tight')
plt.show()