# The following program will read two numbers
# and multiply the first by 2.
# Then it will increase the second number  by one
# and  place the sum of the two numbers in the variable res.
# After all this the program will raise the value in res to the
# power of 3
# and print the result.
first_num = int(input("please type a number "))
second_num = int(input(" dose it matter what I write here ? NO  "))
first_num *= 2 #GR8 almost ...
second_num += 1 # something is missing NOT ANYMORE
res = first_num + second_num # you DON'T need to change something here
res **= 3
print(res)