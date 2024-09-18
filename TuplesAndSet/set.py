set1 = set()
set2 = {1,2,3}
list1 = [4,5,6]
set3 = set(list1)
print(set3)
print(set2)
print(set1)
set1.add("k")
print(set1)
word = "Koala"
set4 = set(word)
print(set4)

set9 = {i*2 for i in range(9)}
set8 = {i*2%3 for i in range(9)}
l8 = [i*2%3 for i in range(9)]

print(set9)
print(set8)
print(l8)
