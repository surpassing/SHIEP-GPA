# encoding = utf-8
#
# SHIEP 总学分，算数平均分,绩点等快速计算。
# Sam 2014-6-20 毕业后第一天写此脚本以用来算出自己的最好看绩点形式 :D
#
# 挂过科的情况本人未测试,0学分科目不在计算范围内。
# SHIEP-GPA-CALCULATOR version 1.5 with python 3.3
# 使用方法:复制成绩页面所有内容到本地文档，有重修科目选择取得最高分的一项，低的那一行全部删除，与本程序放置到同一个文件夹中,运行py。

type_in = input("请输入文件名(请注意有无后缀,建议使用纯文件不使用txt因为未测试过后者!): ")
doc_path = './' + type_in

with open(doc_path,'r',encoding='utf-8') as data:
    text = data.readlines()

def calc():
    course_sum = 0   # 非0学分课程总数
    grade_sum = 0    # 总分数
    credit_sum = 0   # 总学分
    total_ctp = 0

    for each_column in text:
        value = each_column.split()
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

            grade_sum += int(course_grade)  #总分数
            course_sum += 1  #总科目数
            credit_sum += float(course_credit)  #总学分

            #gpa计算用
            credit_times_point = float(course_credit) * float(course_point)  #单项学分乘以绩点
            total_ctp += credit_times_point  #学分乘以绩点的总数

    my_gpa = total_ctp / credit_sum  #  学分乘以绩点的总数除以总学分
    aver_sum = grade_sum / course_sum

    print("显示【学分不等于0】的所有科目(包括换算后的优良中差,ABCD)")
    print('总学分是：', credit_sum)
    print('课程总数是：', course_sum)
    print('总分数是：', grade_sum)
    print('GPA是：', round(my_gpa, 5))
    print('算数平均分是：', round(aver_sum, 3))

calc()
print()
