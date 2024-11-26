number=int(input())
left = number // 1000
sec_left = number // 100%100
third_pair = number // 10 %100
right = number % 100
#print(left,sec_left,third_pair,right)
result=left%7==0 or sec_left%7==0 or right%7==0 or third_pair%7==0
print(f"{result} for the number {number}")