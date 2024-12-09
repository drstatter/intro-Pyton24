base=5
for i in range(base):
    #print space
    for j in range(i):
        print(" ",end='')
    for j in range(base-i):
        print("* ",end='')
    print()