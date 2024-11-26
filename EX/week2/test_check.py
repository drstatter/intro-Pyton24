
ATTENDANCE_PEC=80
HOMEWORK_PEC=70
attendance=80#float(input("Enter the studnet's atendance precentage: "))
hw=90#float(input("Enter the studnet's hw precentage: "))
ex5="yes"#input("Has the  student ex5")
ex5_check= (ex5=="yes") or (ex5=="Yes") or (ex5=="YES")

result=attendance>ATTENDANCE_PEC and hw>=HOMEWORK_PEC and ex5_check
print(f"Can the student participate in the exam? {result}")