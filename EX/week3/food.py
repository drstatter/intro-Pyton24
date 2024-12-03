age=int(input("please enter age"))
weight=int(input("weight"))
height=int(input("height"))
rate= height / weight
message="no food for you"
if age<11 or age > 40 :
    message=message
else:
    if 0.5<=rate<2:
        message="A"
    else:
        if 2<=rate<3.5:
            if 11<=age<=20:
                message="B"
            else:
                if 21<age<40:
                    message="C"
print(message)