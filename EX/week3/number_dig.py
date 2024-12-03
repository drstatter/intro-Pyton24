number=int(input('Number'))
left=number//100
mid=number//10%10
right=number%10
if left+1==mid and mid+1==right:
    print("yes")
else:
    print("no")