base=3
for _ in range(3):
    for i in range(base):
        # print space
        for j in range(base-i-1):
            print(" ", end='')
        # print *
        for j in range(i+1):
            print("* ", end='')
        print()
for _ in range(base):
    print(" "*(base-1)+"*")