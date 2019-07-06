# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:20:57 2019

@author: DELL-1
"""
from pyecharts import Geo
def area_condition(get_all_data):
    get_all_data = get_all_data["work_place"].value_counts()
    del get_all_data['香港特别行政区']
    del get_all_data['澳门特别行政区']
    del get_all_data['庆阳']
    del get_all_data['延边']
    geo = Geo("城市分布情况",
                  title_color="#fff",
                  title_pos="center",
                  width = 800,
                  height = 800,
                  background_color="#404a59")


    attr = get_all_data.index
    value = get_all_data.values
    
    geo.add("",
            attr,
            value,
            type = "effectScatter",
            visual_range=[0,400],
            maptype="china",
            visual_text_color = "#fff",
            geo_normal_color = "#080808",
            geo_emphasis_color = "#FFFF00",
            symbol_size= 6,
            border_color = "#FFFFFF",
            effect_scale = 5,
            is_visualmap=True,
            is_roam = True)
    geo.render("C:/WeSite/DataCharts/岗位概况/岗位-城市分布图.html",pixel_ratio=0.5)
    geo.render("C:/WeSite/DataCharts/岗位概况/岗位-城市分布图.png",pixel_ratio=0.5)
    #geo.show_config()

