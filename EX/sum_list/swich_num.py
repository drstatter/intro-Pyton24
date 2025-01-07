number=1234567
res=0
counter=1
while number>=10:
    left=number%10
    number//=10
    right=number%10
    number //= 10
    two_dig=left*10+right
    res=res+two_dig*counter
    counter*=100
if number>0:
    res+=number*counter
print(res)
