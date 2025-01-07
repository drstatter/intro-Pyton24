
num=72456
save_num=num
result=0
count=1
while num>0:
    dig=num%10
    num//=10
    if dig%2==0:
        result+=dig*count
        count *= 10
print(result)