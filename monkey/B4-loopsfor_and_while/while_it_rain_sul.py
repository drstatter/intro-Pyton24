#This program will print "It's rain if the temp is less than 10
# and you know the temp will go up by one until it will stop raining

temp=int(input("please type the temperature"))
while (temp < 10):
    print("its raining ")
    temp+=1
print("its not raining anymore")