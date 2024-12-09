

number=1234
new_num=0
while number>0:
    new_num*=10
    dig=number%10
    new_num+=dig
    number//=10
print(new_num)