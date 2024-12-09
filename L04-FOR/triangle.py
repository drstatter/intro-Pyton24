trinagle_size=5
#
# for i in range(trinagle_size, 0, -1):  #ng by 1 each time
#     for j in range(i):
#         print("*",end='')
#     print()
# for i in range(trinagle_size):
#     for j in range(trinagle_size-i):
#         print("*",end='')
#     print()
for i in range(trinagle_size,0,-1):
    print("*"*i)
