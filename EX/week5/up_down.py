number = int(input("type a number "))
assert (number>=1)
for num in range(1,number):
    print(num,end=',')
for num in range(number,1,-1):
    print(num, end=',')
print(1)
