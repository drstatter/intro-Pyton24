sum=0
number_of_value=-1
EXIT=-1
number=int(input(f"please type the next value in the end type {EXIT} "))
while number!=EXIT:
    sum+=number
    number_of_value+=1
    number=int(input(f"please type the next value in the end type {EXIT} "))
if number_of_value==0:
        print(0)
else:
        print(sum/number_of_value)