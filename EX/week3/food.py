age=30
weight=30
height=10
age1=range(11,21)
age2=range(21,41)
if age >40 or age <11:
    message="no food for you "
else:
    rate = height/weight
    if 0.5<=rate<2 :
        message="A"
    else:
        if 2<=rate<3.5:
            if age in age1:
                message="B"
            else:
                message="C"
        else:
            message=" no food for you!!!"
print(message)





