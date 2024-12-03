number=333
left=number//100
mid=number//10%10
right=number%10
if left==right and left==mid:
    print(f"The number {number} has all the same dig")
else:
    print(f"The number {number} does not have all the same dig")