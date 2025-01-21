def add_update(name_2_grade_dic):
    name=input("Enter student name: ")
    grade=input("Enter student grade: ")
    name_2_grade_dic[name]=grade
def show_average_grade(name_2_grade_dic):
    grade=name_2_grade_dic.values()
    if len(grade)==0:
        return 0
    return sum(grade)/len(grade)



def delete_student(name_2_grade_dic):
    name=input("Enter student name: ")
    if name in name_2_grade_dic:
        del name_2_grade_dic[name]



def main():

    name_2_grade_dic={"Alice":100,"Bob":90}
    while True:
        print("1. Add or Update Student")
        print("2. Delete Student")
        print("3. Show Average Grade")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice=="4":
            break
        if choice == "1":
            add_update(name_2_grade_dic)
        if choice == "2":
            delete_student(name_2_grade_dic)
        if choice == "3":
            show_average_grade(name_2_grade_dic)
    print(name_2_grade_dic)
if __name__ == '__main__':
    main()