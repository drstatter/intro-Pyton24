
number=23714
right_num=number%100
sec_right=number//10%100
sec_left=number//100%100
left_num=number//1000
#print(right_num,sec_right,sec_left,left_num)
res=left_num%7==0 or sec_left%7==0 or sec_right%7==0 or right_num%7==0
print(f"{res} for the number {number}")