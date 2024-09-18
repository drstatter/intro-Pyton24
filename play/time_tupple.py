import time
time1 = time.time()
for _ in range(1000000):
    tu = (1, 2, 3, 4, 5, 6, 7, 8, 9)
time2 = time.time()
for _ in range(1000000):
    mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
time3 = time.time()
print(time2 - time1)
print(time3 - time2)
