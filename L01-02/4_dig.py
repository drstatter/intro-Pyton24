num=int(input("please type number"))
left = num // 1000
left_2 = (num//100)%10
right = num % 10
right_2 = (num%100)//10
#print(left, left_2,right_2,right) # test
print(left + left_2 == (right + right_2)*2)

print(3<5 and 4>6)