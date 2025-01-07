def count_number(listy,num):
    back = 0
    for x in listy:
        if x == num:
            back += 1
    return back
def count_42(listy):
    return count_number(listy, 42)

listy = [1, 2, 3, 42, 5, 42, 42, 42, 7]
print(count_42(listy))