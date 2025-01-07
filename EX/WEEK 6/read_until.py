# num=int(input("type a number"))
# while not(100<=num<1000 and num%7==0):
#     num = int(input("type a number"))

need_numbers=True
while need_numbers:
    num=int(input("type a number"))
    if 100<=num<1000 and num%7==0:
        need_numbers=False