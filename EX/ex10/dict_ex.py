
NO_SUCH_STUDENT=-1
def main():
    students_data = {
        "Alice": {"age": 20, "grades": [85, 90, 78]},
        "Bob": {"age": 22, "grades": [90, 88, 92]},
        "Charlie": {"age": 21, "grades": [150]},
        "Eve": {"age":29, "grades":[]}
    }
    print(get_average_grade(students_data,"Bob"))
    print(get_average_grade(students_data, "Bo"))
    print(get_average_grade(students_data, "Charlie"))
    print(get_average_grade(students_data, "Eve"))
    print(get_all_students_above_age(students_data, 55))
    print(get_students_with_highest_avarage(students_data))

def get_average_grade(data, student_name):
    if student_name not in data:
        return NO_SUCH_STUDENT
    student_dict = data.get(student_name)
    grade_list = student_dict.get("grades")
    if len(grade_list) == 0:
        return 0
    return sum(grade_list) / len(grade_list)

def add_student(students_data, student_name,age,grade):

    students_data[student_name] = {"age": age, "grades": grade}
def get_all_students_above_age(data, age):
    back=list()
    for name,student_dict in data.items():
        if student_dict["age"] > age:
            back.append(name)
    return back
def get_student_with_highest_average(data):
    max_average = 0
    best_student_name = ""
    for name in data.keys():
        current_average = get_average_grade(data, name)
        if current_average > max_average:
            max_average = current_average
            best_student_name = name
    return best_student_name

if __name__ == '__main__':
    main()