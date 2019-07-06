import random

import tool
import position_info as pi

def analyse_data(df_all,
                 degree,
                 experience,
                 expected_place,
                 expected_job,
                 expected_min_salary,
                 expected_company_finance,
                 expected_bonus,
                 id):
    position_num_tip = "根据您的选择，"
    if len(df_all) == 0:
        position_num_tip += "暂无岗位推荐，建议亲改变条件再试一试呢。\n\n"
        if degree == '博士' or degree == '硕士':
            position_num_tip += "由于博士/硕士学历岗位较少，可尝试将学历条件放宽。\n\n"
        if expected_place not in tool.famous_place:
            position_num_tip += "由于您选择了" + expected_place + "地区，该地区岗位较少，推荐选择以下需求量大的地区：\n"
            for fp in tool.famous_place:
                position_num_tip += fp + " "
            position_num_tip += "\n\n"
    else:
        position_num_tip += "我们为初步您找到合适职位信息" + str(len(df_all)) + "条。\n\n"

        job_info = "招聘信息如下：\n"
        i = 0
        for data in df_all.values:
            job_info += "编号：" + str(i) + \
                        "\t职位名：" + str(data[0]) + \
                        "\t公司名：" + str(data[6]) + \
                        "\t招聘链接：" + str(data[11]) + "\n"
            i = i + 1
            if i >= 10:
                break
        if i == 10:
            job_info += "岗位信息过多，只显示10条以供参考\n\n"

        recommend_tip = "\n经过多方面考虑，给您推荐以下职位：\n"
        index_dict = {}
        for d in df_all.values:
            #print(d)
            place = d[5]
            for a in tool.area:
                if place in a:
                    place = a[0]
            mixed_index = 0.3 * tool.place_salary_index[place] + \
                          0.2 * tool.place_positionNum_index[place] + \
                          0.1 * tool.company_finance_index[d[8]] + \
                          0.1 * tool.company_scale_index[d[9]] + \
                          0.3 * int(d[2])
            index_dict[mixed_index] = d
        index_dict = dict(sorted(index_dict.items(), key=lambda d:d[0],reverse = True))
        #index_dict = collections.OrderedDict(index_dict)
        #print(index_dict)
        for k,e in index_dict.items():
            recommend_tip += "\t职位名：" +  str(e[0]) + \
                             "\t招聘链接：" + str(e[11]) + "\n" +\
                             "\t公司名："+ str(e[6]) + \
                             "\t该职位最高薪资：" + str(e[2]) + "k" + \
                             "\t公司规模："+str(e[9]) + \
                             "\t公司融资情况："+str(e[8])+"\n\n"
            break;

    position_duty_tip = "您选择的职位有以下职责和要求：\n" + pi.duty_dict[expected_job]+"\n\n"

    chicken_soup_len = len(tool.chicken_soup)
    chicken_soup = "心灵鸡汤："+tool.chicken_soup[random.randint(0,chicken_soup_len-1)] + "\n"


    file_name = "C:/GraduateSchedule/schedule.txt"
    with open(file_name, 'w') as f:
        f.write(position_num_tip)
        f.write(job_info)
        f.write(recommend_tip)
        f.write(position_duty_tip)
        f.write(chicken_soup)
