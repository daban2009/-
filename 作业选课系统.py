# Author:ZHJ

import sys,os
import shelve

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)


class MainView(object):
    def __init__(self):
        pass

    def run(self):
        while True:
            info = '''
            ┏****************┓
            ┃欢迎进入选课系统┃
            ┗****************┛
            ┏━━━━━━━━┓
            ┃   1.学员入口   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   2.讲师入口   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   3.管 理 员   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   q.退    出   ┃
            ┗━━━━━━━━┛
             '''
            print('\033[34m{0}\033[0m'.format(info))
            selection = input("\033[1;33m请输入您的选择：\033[0m").strip()
            # print(selection)
            if selection == "1":
                student_view_obj = StudentView()
                student_view_obj.run()
            elif selection == "2":
                teacher_view_obj = TeacherView()
                teacher_view_obj.run()
            elif selection == "3":
                admin_view_obj = AdminView()
                admin_view_obj.run()
            elif selection == "q":
                sys.exit()
            else:
                print("\033[1;31m您的输入不正确。\033[0m")


class StudentView(object):
    def run(self):
        while True:
            info = '''
            ┏━━━━━━━━┓
            ┃    学    员    ┃
            ┗━━━━━━━━┛
            ┏━━━━━━━━┓
            ┃   1.注    册   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   2.交 学 费   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   r.返上一级   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   q.退    出   ┃
            ┗━━━━━━━━┛
                '''
            print('\033[34m{}\033[0m'.format(info))
            selection = input("\033[1;35m 请输入你的选择：\033[0m").strip()
            if selection == "1":
                self.enroll()
            elif selection == "2":
                self.pay_tuition()
            elif selection == "r":
                break
            elif selection == "q":
                sys.exit()
            else:
                print("\033[1;31m您的输入不正确。\033[0m")
    def enroll(self):
        school_data = shelve.open(BASE_DIR + r"\school_data",writeback=True)
        # print(self.school_data)
        name = input("请输入您的名字：")
        age = input("请输入您的年龄：")
        sex = input("请输入您的性别：")
        print("\033[1;32m可选择的校区：\033[0m")
        for i in school_data:
            print('\033[1;34m           {}\033[0m'.format(i))
        select_school = input("请选择学校")
        if select_school in school_data:
            # print(school_data[select_school].course)
            print("\033[1;32m可选择的班级：\033[0m")
            for i in school_data[select_school].classes:
                print('\033[1;34m           {}\033[0m'.format(i))
            select_classes = input("请选择班级")
            if select_classes in school_data[select_school].classes:
                school_data[select_school].classes[select_classes].add_students(name,age,sex)
                school_data[select_school] = school_data[select_school]
                print("\033[1;31m学员添加成功\033[0m")
            else:
                print("\033[1;31m输入的班级不存在!\033[0m")
        else:
            print("\033[1;31m输入的学校不存在!\033[0m")
        school_data.close()
    def pay_tuition(self):
        pass
class TeacherView(object):
    # def __init__(self):
    #     self.school_data = shelve.open(BASE_DIR + r"\school_data")
    #
    # def __del__(self):
    #     self.school_data.close()

    def run(self):
        while True:
            info = '''
            ┏━━━━━━━━┓
            ┃    讲    师    ┃
            ┗━━━━━━━━┛
            ┏━━━━━━━━┓
            ┃   1.查看学员   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   r.返上一级   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   q.退    出   ┃
            ┗━━━━━━━━┛
                '''
            print('\033[34m{}\033[0m'.format(info))
            selection = input("\033[1;35m 请输入你的选择：\033[0m").strip()
            if selection == "1":
                self.see_stu_list()
            elif selection == "r":
                break
            elif selection == "q":
                sys.exit()
            else:
                print("\033[1;31m您的输入不正确。\033[0m")
    def see_stu_list(self):
        school_data = shelve.open(BASE_DIR + r"\school_data")
        print("\033[1;32m可选择的校区：\033[0m")
        for i in school_data:
            print('\033[1;34m           {}\033[0m'.format(i))
        name = input("请选择学校")
        if name in school_data:
            print("\033[1;32m可选择的班级：\033[0m")
            for i in school_data[name].classes:
                print('\033[1;34m           {}\033[0m'.format(i))
            classes = input("请选择班级")
            # print(school_data[name])
            # print(school_data[name].classes)
            # print(school_data[name].classes[classes])
            if classes in school_data[name].classes:
                print("\033[1;32m学员列表：\033[0m")
                for i in school_data[name].classes[classes].students:
                    print('\033[1;34m           {}\033[0m'.format(i))
            else:
                print("\033[1;31m输入的班级不存在!\033[0m")
        else:
            print("\033[1;31m输入的学校不存在!\033[0m")
class AdminView(object):
    # def __init__(self):
    #     self.school_data = shelve.open(BASE_DIR+r"\school_data", writeback=True)

    def __del__(self):
        # self.school_data.close()
        print("看看执行么有")
    def run(self):
        while True:
            info = '''
            ┏━━━━━━━━┓
            ┃    管 理 员    ┃
            ┗━━━━━━━━┛
            ┏━━━━━━━━┓
            ┃   1.创建学校   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   2.创建讲师   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   3.创建班级   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   4.创建课程   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   5.删除学校   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   r.返上一级   ┃
            ┣┉┉┉┉┉┉┉┉┫
            ┃   q.退    出   ┃
            ┗━━━━━━━━┛
                '''
            print('\033[34m{}\033[0m'.format(info))
            selection = input("\033[1;35m 请输入你的选择：\033[0m").strip()
            if selection == "1":
                self.add_school()
            elif selection == "2":
                self.add_teacher()
            elif selection == "3":
                self.add_class()
            elif selection == "4":
                self.add_course()
            elif selection == "5":
                self.del_school()
            elif selection == "r":
                break
            elif selection == "q":
                sys.exit()
            else:
                print("\033[1;31m您的输入不正确。\033[0m")
    def add_teacher(self):
        school_data = shelve.open(BASE_DIR + r"\school_data", writeback=True)
        print("\033[1;32m可选择的校区：\033[0m")
        for i in school_data:
            print('\033[1;34m           {}\033[0m'.format(i))
        name = input("请选择学校")
        if name in school_data:
            print(school_data[name].teacher)
            tch_name = input("请输入姓名")
            tch_age = input("请输入年龄")
            tch_sex = input("请输入性别")
            tch_salary = input("请输入收入")

            school_data[name].add_teacher(tch_name,tch_age,tch_sex,tch_salary)
            school_data[name] = school_data[name] #加入了老师的学校写入文件
        else:
            print("\033[1;31m输入的学校不存在!\033[0m")
        school_data.close()
    def add_school(self):
        school_data = shelve.open(BASE_DIR + r"\school_data", writeback=True)
        name = input("请输入学校名")
        school_data[name] = School(name)
        school_data.close()
    def del_school(self):
        school_data = shelve.open(BASE_DIR + r"\school_data", writeback=True)
        print("\033[1;32m可选择的校区：\033[0m")
        for i in school_data:
            print('\033[1;34m           {}\033[0m'.format(i))
        name = input("请输入学校名")
        if name in school_data:
            del school_data[name]
        else:
            print("\033[1;31m输入的学校不存在!\033[0m")
        school_data.close()
    def add_course(self):
        school_data = shelve.open(BASE_DIR + r"\school_data", writeback=True)
        print("\033[1;32m可选择的校区：\033[0m")
        for i in school_data:
            print('\033[1;34m           {}\033[0m'.format(i))
        name = input("请选择学校")
        if name in school_data:
            print(school_data[name].course)
            cour_name = input("请输入名称")
            cour_time = input("请输入学习周期")
            cour_price = input("请输入价格")

            school_data[name].add_course(cour_name, cour_time, cour_price)
            school_data[name] = school_data[name]  # 加入了课程的学校写入文件
        else:
            print("\033[1;31m输入的学校不存在!\033[0m")
        school_data.close()
        #可能是没有正常关闭导致
    def add_class(self):
        school_data = shelve.open(BASE_DIR + r"\school_data", writeback=True)
        print("\033[1;32m可选择的校区：\033[0m")
        for i in school_data:
            print('\033[1;34m           {}\033[0m'.format(i))
        name = input("请选择学校")
        if name in school_data:
            class_name = input("请输入班级名")
            print("\033[1;32m可选择老师：\033[0m")
            for i in school_data[name].teacher:
                print('\033[1;34m           {}\033[0m'.format(i))
            class_teacher = input("请选择老师")
            if class_teacher in school_data[name].teacher:

                print("\033[1;32m可选择课程：\033[0m")
                for i in school_data[name].course:
                    print('\033[1;34m           {}\033[0m'.format(i))
                class_course = input("请选择课程")
                if class_course in school_data[name].course:
                    school_data[name].add_class(class_name, class_teacher, class_course)
                    school_data[name] = school_data[name]  # 加入了课程的学校写入文件
                else:
                    print("\033[1;31m输入的课程不存在\033[0m")
            else:
                print("\033[1;31m输入的老师不存在\033[0m")
        else:
            print("\033[1;31m输入的学校不存在!\033[0m")
        school_data.close()

class School(object):
    def __init__(self, name):
        self.name = name
        self.course = {}
        self.classes = {}
        self.teacher = {}

    def add_class(self, name, teacher, course):
        class_obj = Class(name, teacher, course)
        self.classes[name] = class_obj

    def add_course(self, name, time, price):
        course_obj = Course(name, time, price)
        self.course[name] = course_obj

    def add_teacher(self, name, age, sex, salary):
        teacher_obj = Teachers(name, age, sex, salary)
        self.teacher[name] = teacher_obj


class Class(object):
    def __init__(self, name, teacher, course):
        self.name = name
        self.teacher = teacher
        self.course = course
        self.students = {}

    def add_students(self, name, age, sex):
        students_obj = Students(name, age, sex)
        self.students[name] = students_obj


class Course(object):
    def __init__(self, name, time, price):
        self.name = name
        self.time = time
        self.price = price


class Teachers(object):
    def __init__(self, name, age, sex, salary):
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary


class Students(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


m1 = MainView()
m1.run()