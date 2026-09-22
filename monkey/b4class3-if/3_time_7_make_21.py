# In this program we will check whether a number typed
# by the user is divisible by 21 (ie divisible by 3 and 7)
# or is divisible by only one of them (3 or 7) or none of them.
num_to_check=int(input("please type a number "))
#num % 3 ==0 mean that num is divisible by 3
if num_to_check % 3 == 0 and num_to_check % 3 == 1 :  # wait what ?
    print(f"{num_to_check} is divisible by both 3 and 7")
# do we need this else ? try to remove it (and fix the indentation :))
else:
    if num_to_check == 42 or num_to_check % 7 == 0:  # or what ?
        print(f"{num_to_check} is divisible by only by one of the numbers 3,7")
    else:
        print("what happe here ? ")  #  add a measage 