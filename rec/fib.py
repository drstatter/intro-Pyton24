def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
#print(fib(40))
def fib_iter(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return b

print(fib_iter(100))