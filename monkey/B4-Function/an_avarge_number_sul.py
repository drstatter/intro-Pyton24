# make this program work. look on the script in lines 26-33
# and try to figure out what is the problem. Basicly
# there is a function named find max that is working correctly you should fix
# the function named find_min



# here is a function that  will get 3 numbers and return the max
# Initialize my_max with the value of num1.
# Compare num2 with my_max; if num2 is greater, update my_max.
# Compare num3 with my_max; if num3 is greater, update my_max.
# Return the value of my_max.

def find_max(num1,num2,num3):
    my_max = num1
    if num2 > my_max :
         my_max = num2
    if num3 > my_max :
         my_max = num3
    return my_max

# now write a function that find the miniman out of 3 numbers
def find_min(num1,num2,num3) :
    my_min = num1
    if num2 <  my_min :
        my_min = num2
    if num3 < my_min :
        my_min = num3
    return my_min

number1=int(input("please type a number "))
number2=int(input("please type a number "))
number3=int(input("please type a number "))
the_max=find_max(number1,number2,number3)
#is somthing missing in the def of find_min line ?
the_min=find_min(number1,number2,number3)
# did you return the result of the find min ?
print(f"the max is {the_max} and the min is {the_min}")