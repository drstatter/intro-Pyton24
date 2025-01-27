def rec_num(num):
    if num < 1:
        return

    rec_num(num - 1)
    print(num, end=" ")
rec_num(5)