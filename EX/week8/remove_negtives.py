def remove_neg(listy):
    for x in listy:
        if x < 0:
            listy.remove(x)
    # no need for returning
    return listy
def find_max_min(num1,num2,num3):
    if num1>num2 and num1 > num3:
        max=num1
    else:
        if num2>num3:
            max=num2
        else:
            max=num3
    my_min=min(num1,num2,num3)
    return max,my_min
def main():
    a=3
    b=9
    c=5
    a,b=find_max_min(a,b,c)
    print(a,b,c)

# test
my_list = [1, -2, 3, -4, 5]
remove_neg(my_list)
print(my_list)

main()