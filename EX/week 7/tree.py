base=3
for _ in range(3):
    for i in range(1,base+1):
        #space
        for _ in range(base-i):
            print(" ",end='')
        #star
        for _ in range(i):
            print("* ",end='')
        print("")
for _ in range(base):
    #space
    for _ in range(base-1):
        print(" ",end='')
    #star
    print("*")

