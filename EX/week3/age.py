

YOUNG=18
OLD=65
age=int(input("type your age "))
adult_range=range(YOUNG,OLD+1)
if age<YOUNG:
    message="you are young"
else:
    if age in adult_range:
        message="you are adult"
    else:
        message="you are old"
print(message)