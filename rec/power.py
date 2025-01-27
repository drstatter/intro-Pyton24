def power(base, exponent):
    if exponent <=0:
        return 1
    else:
        temp = power(base, exponent//2)
        if exponent % 2 == 0:
            return temp * temp
        else:
            return temp *  temp* base
print(power(2, 5))
print(power(2, 4))