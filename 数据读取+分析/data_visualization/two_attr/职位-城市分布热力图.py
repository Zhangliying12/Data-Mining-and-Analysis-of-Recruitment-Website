from pyecharts import Geo
#from pyecharts.render import make_snapshot
#from snapshot_phantomjs import snapshot

#import clr
#clr.AddReference('WebPhoto')
#from WebPhoto import *

import collections
import tool
df_all = tool.read_and_clean_all_data()
w_dict = collections.Counter(df_all['work_place'])

work_place_dict = {}
for a in tool.area:
    df = df_all[df_all['work_place'].isin(a)]
    work_place_dict[a[0]]=len(df)


geo = Geo("岗位-城市分布图", title_pos='center', title_top='0', width=900, height=600, title_color="#fff", background_color="#404a59")
#attr = city_com_last['job_city']
#value = city_com_last['count']
del w_dict['香港特别行政区']
del w_dict['澳门特别行政区']
del w_dict['庆阳']
geo.add("", w_dict.keys(), w_dict.values(), is_visualmap=True, visual_range=[0, 180], visual_text_color="#fff", symbol_size=15)
geo.render(path="岗位-城市分布图.html",pixel_ratio=1)
