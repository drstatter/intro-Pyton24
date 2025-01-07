TOP=10  000
for num in range(1,TOP):
    sum = 0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    sum2=0
    for i in range(1,sum):
        if sum%i==0:
            sum2+=i
    if sum2==num and sum>num :
        print(num,sum)