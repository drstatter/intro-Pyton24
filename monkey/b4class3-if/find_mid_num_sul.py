# this program will read 3 numbers from the user and print the middle one
# on input 9,14,5 the output will be 9
number1 = int(input("please type a number "))
number2 = int(input("please type a number "))
number3 = int(input("please type a number "))
if number3 > number2:
    if number1 > number3:
        print(number3)
    else:
        if number1 > number2:
            print(number1)
#2>3
else:
    if number1 > number2:
        print(number2)
    else:
        if number1 > number3:
            print(number1)
        else:
            print(number3)
