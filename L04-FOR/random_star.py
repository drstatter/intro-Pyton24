import random

number_star=random.randint(1,12)
print(number_star)
for _ in range(number_star):
    print("*", end=" ")