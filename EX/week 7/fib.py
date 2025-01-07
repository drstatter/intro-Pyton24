num1=1
num2=2
size=8
for _ in range(size-1):
    next_num=num1+num2
    num1=num2
    num2=next_num
print(next_num)