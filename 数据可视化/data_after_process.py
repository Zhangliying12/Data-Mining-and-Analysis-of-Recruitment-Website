# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 08:54:52 2019

@author: DELL-1
"""

import data_from_mysql
import data_preprocess

def data_after_process_():
    get_data_all = data_from_mysql.get_data_from_mysql()

    get_data_all = data_preprocess.pass_common(get_data_all)

    get_data_all = data_preprocess.data_null(get_data_all)

    get_data_all = data_preprocess.pass_item(get_data_all)

    get_data_all = data_preprocess.data_salary_max(get_data_all)

    print(len(get_data_all))
    return get_data_all


def one_table_process(data):
    data = data_preprocess.pass_common(data)

    data = data_preprocess.data_null(data)

    data = data_preprocess.pass_item(data)

    data = data_preprocess.data_salary_max(data)
    
    return data