
number=12144
left_dig=number//10000
sec_left=number//1000%10
mid_dig=number//100%10
sec_right=number//10%10
right_dig=number%10
#print(left_dig,sec_left,mid_dig,sec_right,right_dig)
res=left_dig==sec_left or sec_left==mid_dig or mid_dig==sec_right or sec_right==right_dig
print(f"the number {number} is {res}")