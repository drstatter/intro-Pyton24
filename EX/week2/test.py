CLASS_ATTEND=80
HOMEWORK_PEC=70
EX5_TRUE="yes"
attend=float(input("Enter the stunds    vdvgdsfg"))
hw=float(input("Enter the hw    vdvgdsfg"))
ex5=input("ex5")
ex5_handed=(ex5=="yes" or ex5=="yes " or ex5=="Yes")
result=attend>=CLASS_ATTEND and hw>=HOMEWORK_PEC and ex5_handed
print(f"Can the student participate in the exam? {result}")