my_list=[4,6,8,11,5,3]
# add 7 to the end of the list
#how do say add in an arrogant way ? maybe append ?

my_list.append(7)
print(my_list)
# replace the first item with 1
my_list[0] = 1
print(my_list)
# remove the value 6 from the list
my_list.remove(6)
print(my_list)
# print the size of the list
print(len(my_list))

# create a new list with the same values multiped by 2
new_list = [x * 2 for x in my_list] # you can use list comprehension
new_list2 = list()
for number in my_list:
     new_list2.append(number * 2) # you can use a for loop

print(new_list)
print(new_list2)

