def main():
    students_data = {
        "Alice": {"age": 20, "grades": [85, 90, 80]},
        "Bob": {"age": 22, "grades": []},
        "Charlie": {"age": 21, "grades": [95, 100, 89]}
    }
    print(get_average_grade(students_data, "Alice"))
    print(get_average_grade(students_data, "Bob"))
    print(get_average_grade(students_data, "Bb"))
    add_student(students_data,"Eve",28,[10])
    print(get_average_grade(students_data, "Eve"))
    print(get_students_with_highest_avarage(students_data))


def get_average_grade(students_data,student_name):
    student_dic=students_data.get(student_name)
    if student_dic is None:
        return -1
    else:
        grades = student_dic["grades"]
        if len(grades) == 0:
            return -2
        else:
            return sum(grades)/len(grades)

def add_student(students_data,student_name,age,grades):
    students_data[student_name]={"age":age,"grades":grades}

def get_all_students_above_age(students_data,age):
    back=list()

    for name,student_dic in students_data.items():
        if student_dic["age"]>age:
            back.append(name)
    return back
def get_students_with_highest_avarage(students_data):
    max_grade=0
    max_student=""
    for name in students_data.keys():
        current_student_ave=get_average_grade(students_data,name)
        if current_student_ave>max_grade:
            max_grade=current_student_ave
            max_student=name
    return max_student
if __name__ == '__main__':
    main()