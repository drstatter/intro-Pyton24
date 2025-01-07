start=1#int(input("first "))
sec=2#int(input("second "))
n=8#int(input("N "))
for _ in range(n):
    next=start+sec
    start=sec
    sec=next
    print(next,end= " ")
print(next)