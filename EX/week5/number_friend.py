num=220
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
#print(sum)
sum2=0
for i in range(1,sum):
    if sum%i==0:
        sum2+=i
#print(sum2)
if sum2==num:
    print(num,sum)
