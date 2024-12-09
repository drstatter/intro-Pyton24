number_of_odd=0
for _ in range(10):
    num=int(input("Enter a number: "))
    if num%2!=0:
        number_of_odd+=1
print (number_of_odd)