#input
number=int(input('Number '))
#check input
if number<0:
    exit()
#logic
for x in range(0,number-1,2):
     print(x, end=",")
#last case
if number%2==0:
    print(number)
else:
    print(number-1)
