def sum_dig_num(number):
    back=0
    while number>0:
        back+=number%10
        number//=10
    return back
