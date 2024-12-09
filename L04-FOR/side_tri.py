base=4
#row
for i in range(base):
    #print space
    for j in range(base-1-i):
        print(" ",end='')
    #print *
    for j in range(i+1):
        print("*",end='')
    print()
   # print(" "*(base-1-i)+"*"*(i+1))