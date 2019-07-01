from pyecharts import Geo
#from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot
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
geo.render("岗位-城市分布图.html")

geo = Geo("岗位-城市分布热力图", title_pos='center', title_top='0', width=900, height=600, title_color="#fff", background_color="#404a59")
del work_place_dict['香港特别行政区']
del work_place_dict['澳门特别行政区']
#del work_place_dict['庆阳']
geo.add("", work_place_dict.keys(), work_place_dict.values(), type="heatmap", is_visualmap=True, visual_range=[0, 30], visual_text_color="#fff")
geo.render("岗位-城市分布热力图.html")

#make_snapshot(snapshot,geo.render(),'岗位-城市分布热力图.png')