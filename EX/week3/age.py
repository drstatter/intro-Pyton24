YOUNG=18
OLD=65
age=int(input("Enter age "))
if age<YOUNG:
    print("You are to young")
else :
    if age<=OLD:
        print("You are an adult")
    else :
        print("You are an elder")