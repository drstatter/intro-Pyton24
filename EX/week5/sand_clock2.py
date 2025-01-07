base=5
for raw in range(base):
    #space
    for i in range(raw):
        print(" ", end="")
    #star
    for j in range(base-raw):
        print("* ", end="")
    print()

for raw in range(base-1,-1,-1):
    #space
    for i in range(raw):
        print(" ", end="")
    #star
    for j in range(base-raw):
        print("* ", end="")
    print()
