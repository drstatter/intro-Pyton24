

num1=37
num2=81
save1=num1
save2=num2
result=0
count=0
while num1>0:
    dig1=num1%10
    dig2=num2%10
    num1//=10
    num2//=10
    number=dig1*10+dig2
    result+=number*(100**count)
    count+=1
print(result)