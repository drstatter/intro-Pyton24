number=14641
left_dig=number//10000
right_dig=number%10
sec_right=number//10%10
sec_left=number//1000%10
#print(left_dig, sec_left,sec_right,right_dig)
is_poly=left_dig==right_dig and sec_left==sec_right
is_divisible_by_6=(number%6==0)
print(f"{is_divisible_by_6 and is_poly} for the number {number}")
#print(is_poly, is_divisible_by_6)