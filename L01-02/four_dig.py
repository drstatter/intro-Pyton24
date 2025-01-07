num=int(input("type a number "))
right_dig=num%10
num//=10
sec_right=num%10
num//=10
sec_left=num%10
num//=10
left_dig=num%10
print(left_dig,sec_left,sec_right,right_dig)
answer=(left_dig+sec_left)==(2*(right_dig+sec_right))
print(answer)