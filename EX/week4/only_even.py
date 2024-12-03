number=1234567
new_number=0
loc=0
while number>0:
    digit=number%10
    number//=10
    if digit%2==0:
        new_number=new_number+(digit*10**loc)
        loc+=1
print(new_number)