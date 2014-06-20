# encoding = utf-8
# shiep查询成绩系统平均分,绩点等计算
# Sam 2014-6-18
# 在分数页面复制该页内容到本地文件，与本文件放置在同一个文件夹中并重命名为data(无后缀)
# 手动筛选data文件中的所有重修科目(删掉分数低的，留一个高的即可)！！！
# 0学分科目不在计算范围内
# 版本1

with open('./data','r',encoding='utf-8') as data:
    text = data.readlines()

def calc():
    course_sum = 0   # 非0学分课程总数
    grade_sum = 0    # 总分数
    credit_sum = 0   # 总学分
    total_ctp = 0

    for each_column in text:
        value = each_column.split()
#        course_no = value[1]     # 课号
#        course_name = value[2]   # 课程名
#        course_period = value[9] # 学期
#       take_it_over = value[8]
        course_credit = value[4]  # 学分
        course_grade = value[5]   # 分数
        course_point = value[6]   # 绩点

        if course_credit != '0':
            if course_grade == ('优' or 'A'):
                course_grade = '90'
            elif course_grade == '良' or course_grade == 'B':
                course_grade = '80'
            elif course_grade == ('中' or 'C'):
                course_grade = '70'
            elif course_grade == ('及格' or 'D'):
                course_grade = '60'

            grade_sum += int(course_grade)  #总分数
            course_sum += 1  #总科目数
            credit_sum += float(course_credit)  #总学分

            #gpa计算用
            credit_times_point = float(course_credit) * float(course_point)  #单项学分乘以绩点
            total_ctp += credit_times_point  #学分乘以绩点的总数

    my_gpa = total_ctp / credit_sum  #  学分乘以绩点的总数除以总学分
    aver_sum = grade_sum / course_sum
    aver_point = (aver_sum - 50) / 10

    print("显示学分不等于0的所有科目(包括换算后的优良中差,ABCD)")
    print('总学分是：', credit_sum)
    print('非0学分课程总数是：', course_sum)
    print('非0学分分数总数是：', grade_sum)
    print('非0学分课程的GPA是：', round(my_gpa, 5))
    print('非0学分课程的算数平均分是：', round(aver_sum, 3))
    print('非0学分课程的折合绩点是：', round(aver_point, 3))

calc()
print()
print()

'''
def other_calc():
    sub_no = 0
    score_sum = 0

    for each_column in text:
        course = each_column.split()
        point = course[4]
        score = course[5]

        if score.isdigit() and point != '0':
            score_sum += int(score)
            sub_no += 1

    print("显示学分不等于0，且有实际分数的科目(不包括优良中差，ABCD)")
    print("总分数: " + str(score_sum))
    print("科目数: " + str(sub_no))
    print("平均分: " + str( score_sum * 1.0/sub_no))

other_calc()
'''