base=4
my_triangle=""
for i in range(1,base+1):
    #space
    for j in range(base-i):
        my_triangle+=" "
    for j in range(i):
        my_triangle+="*"
    my_triangle+="\n"
for i in range(base-1,0,-1):
    for j in range(base-i):
        my_triangle += " "
    for j in range(i):
        my_triangle += "*"
    my_triangle += "\n"
#print (my_triangle)
st="   *\n"+"  **\n"+" ***\n"+"****\n"+" ***\n"+"  **\n"+"   *\n"
if my_triangle==st:
    print("true")
print(my_triangle)
