
def get_average_grade(data, student_name):
    student_dic=data.get(student_name)
    if student_dic is None:
        return "no"
    else:
        grades=student_dic.get("grades")
        if len(grades)==0:
            return "no grades"
        return sum(grades)/len(grades)
def get_all_students_above_age(data, age):
    back=list()
    for name,student_dic in data.items():
        if student_dic.get("age") > age:
            back.append(name)
    return back
def add_student(data, student_name,age,grades):
    data[student_name]={"age":age,"grades":grades}
   
def main():
    students_data = {
        "Alice": {"age": 20, "grades": [85, 90, 80]},
        "Bob": {"age": 22, "grades": []},
        "Charlie": {"age": 21, "grades": [95, 100, 89]}
    }
    add_student(students_data,"Eva",29,[100])
    print(get_average_grade(students_data, "Eva"))
    print(students_data)
    print(get_all_students_above_age(students_data, 20))
if __name__ == '__main__':
    main()