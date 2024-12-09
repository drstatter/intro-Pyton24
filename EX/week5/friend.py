top=10000
for num in range(top):
    # find the div and sum
    sum=0
    for i in range(1,num):
        if num%i == 0:
            sum += i
    #check sum
    if sum>num:
        new_sum=0
        for i in range(1,num):
            if sum%i == 0:
                new_sum += i
        if new_sum==num:
            print(num,sum)
    #print