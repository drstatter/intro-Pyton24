
num=int(input(''))
right=num%10
sec_right=(num//10)%10
middle=num//100%10
sec_left=num//1000%10
left=num//10000
print(left, sec_left,middle, sec_right, right) # test
result=left==sec_left or sec_left==middle or middle==sec_right or sec_right==right
print(f"The number {num} is {result}")