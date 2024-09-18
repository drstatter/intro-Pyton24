string1 = "koala"

listy = ["dog", "cat", "koala"]
tuple1 = ("pig", "lion", "one more koala")

# adding
string1 = string1 + "42"
listy = listy + ["42"]
tuple1 = tuple1 + ("42",)
print(string1)
print(listy)
print(tuple1)
# slicing
print(string1[1:3])
print(listy[1:3])
print(tuple1[1:3])

# iter

for x in string1:
    print(x + "#", end="")
print()
for x in listy:
    print(x + "#", end="")
print()
for x in tuple1:
    print(x + "#", end="")
print()
temp=sorted(tuple1)
print("&&&&",temp)

