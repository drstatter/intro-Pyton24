def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def choose(n, k):
    if n==1:
        return 1
    if k==n or k==0:
        return 1
    return choose(n-1, k) + choose(n-1, k-1)

def choose(n,k):
    if n==k:
        return 1
    elif k==1:
        return n
