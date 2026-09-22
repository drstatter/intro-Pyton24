#Here we will write the first function like in code monkey
#combining few commends to one (like turn to banana and go to banana )

# this function get a number in the input (a variably named number)
# and print 42 is a great number if its  42 :)
# later on we use  the function 5 times


def im_a_function(number) :
    # implementation here
    print(" start function")
    if number : # if what ?
        print(f"{number} is a great number")
    else :
        print(f"well you can do better then {number} ")

for _ in range(5) :
    num1 = int(input("please type a number "))
    # how to use the function ? maybe  im_a_function(num1)?