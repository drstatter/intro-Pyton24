

num1=37
num2=48
new_number=0
loc=0
while num1>0:
    dig=num2%10
    num2//=10
    new_number+=(dig*(10**loc))
    loc+=1
    dig = num1 % 10
    num1 //= 10
    new_number += (dig * (10 ** loc))
    loc += 1
print(new_number)