


def add_update(name_2_grade):
    name=input("enter student name")
    grade=int(input("enter student grade (0-100)"))
    name_2_grade[name]=grade
def delete_student(name_2_grade):
    name=input("enter student name to delete ")
    if name in name_2_grade:
        del name_2_grade[name]
    else:
        print("student not found")


def print_ave(name_2_grade):
    grade=name_2_grade.values()
    if len(grade)==0:
        print("0")
    else:
        print(sum(grade)/len(grade))


def main():
    name_2_grade={"KOALA":100,"Pibi":90}

    while True:
        print("1. Add or Update Student")
        print("2. Delete Student")
        print("3. Show Average Grade")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_update(name_2_grade)
        if choice == "2":
            delete_student(name_2_grade)
        if choice == "3":
            print_ave(name_2_grade)
        if choice == "4":
            break
    print(name_2_grade)
if __name__ == '__main__':
    main()