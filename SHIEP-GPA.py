# encoding = utf-8
#
# SHIEP 总学分，总绩点，算数平均分，平均绩点GPA等快速计算。
# Sam 2014-6-20所写 毕业后第一天写此脚本以用来算出自己的最好看绩点形式 :D
#
# 挂过科的情况本人未测试(去掉不规则的行数试试)，免听重修的可以使用本脚本进行计算，0学分科目不在计算范围内。
# SHIEP-GPA-CALCULATOR version 2.0 beta with python 3.3 6-21-2014
# 使用方法:复制成绩页面所有表格内内容到本地文档，与本程序放置到同一个文件夹中,运行py。

course_in_all = {}

def all_start():
    global course_in_all
    global text
    course_in_all = {}
    type_in = input("请输入文件名(请注意有无后缀): ")
    doc_path = './' + type_in

    with open(doc_path,'r',encoding='utf-8') as data:
        text = data.readlines()

def make_dict():
    global course_in_all
    for each_column in text:
        value = each_column.split()
#       take_it_over = value[9]   # 是否重修
        course_num = value[1]     # 课号
        course_credit = value[4]  # 学分
        course_grade = value[5]   # 分数
        course_point = value[6]   # 绩点

        if course_credit != '0':
            if course_grade == '优' or course_grade == 'A':
                course_grade = '90'
            elif course_grade == '良' or course_grade == 'B':
                course_grade = '80'
            elif course_grade == '中' or course_grade == 'C':
                course_grade = '70'
            elif course_grade == '及格' or course_grade == 'D':
                course_grade = '60'

            if course_num not in course_in_all:
                course_in_all[course_num] = [course_credit, course_grade, course_point]
            else:
                  if course_grade >= course_in_all[course_num][1]:
                      course_in_all[course_num][1] = course_grade
                      course_in_all[course_num][2] = course_point

def calc():
    course_sum, credit_sum, grade_sum, point_sum = 0, 0, 0, 0
    total_ctp = 0

    for i in course_in_all:
        course_sum += 1
        credit_sum += float(course_in_all[i][0])  # 学分
        grade_sum += float(course_in_all[i][1])   # 分数
        point_sum += float(course_in_all[i][2])   # 绩点

        # gpa计算用
        credit_times_point = float(course_in_all[i][0]) * float(course_in_all[i][2])  # 单项学分乘以绩点
        total_ctp += credit_times_point  # 学分乘以绩点的总数

       # 平均分计算用
        aver_point = grade_sum / course_sum
        if  aver_point >= 90:
            aver_point_final = 4
        else:
            aver_point_final = (aver_point - 50) / 10

    my_gpa = total_ctp / credit_sum  # 学分乘以绩点的总数除以总学分

    print(course_sum, credit_sum, grade_sum, point_sum)
    print("上海电力外语系2010级某只求高GPA的路过，本脚本显示【学分不等于0】的所有科目(包括换算后的优良中差,ABCD)")
    print("鸣谢:所有给我高分的那些老师们！有机会的话在3.0里加入教师统计给你们统统赞一个，我都记得的。")
    print('总学分是：', credit_sum)
    print('总课程数是：', course_sum)
    print('总分数是：', grade_sum)
    print('GPA是：', round(my_gpa, 5))
    print('算数平均分是：', round(aver_point, 3), ', 即', round(aver_point_final, 5))

if __name__ == '__main__':
    while True:
        a = input('输入y开始计算,n退出： ')
        if a == ('y' or 'Y'):
            all_start()
            make_dict()
            calc()
        else:
               exit()
