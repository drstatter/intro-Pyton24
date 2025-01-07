
num1=245
num2=542
save1=num1
save2=num2
answer="YES"
if num1<0 or num2<0 :
    answer="NO"
else:
    while save1>0:
        if save2==0:
            answer="NO1"
            break
        save1=save1//10
        save2=save2//10
    if save2>0:
        answer="NO2"
    # rev num2
    save2 = num2
    res = 0
    while save2 > 0:
        res=(res * 10)+save2%10
        save2 = save2//10
    print(res)
    if res!=num1:
        answer="NO"
print(answer)

for number in range(10,1001):
    #find rev
    save_num=number
    if number%10!=0:
        res = 0
        while number > 0:
            res = (res * 10) + number % 10
            number //= 10
            if res > save_num:
                print(res,save_num)





