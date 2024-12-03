
number=int(input(""))
left_dig=number//10000
right_dig=number%10
sec_left=number//1000%10
sec_right=number//10%10
mid_dig=number//100%10
right_num=sec_right*10+right_dig
print(left_dig,sec_left,sec_right,right_dig)
is_div_6=number%6==0
is_poly=left_dig==right_dig and sec_left==sec_right
#print(is_div_6,is_poly)
print(f"the number {number} is {is_div_6 and is_poly}")