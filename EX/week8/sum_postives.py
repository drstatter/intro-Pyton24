def sum_positive_numbers(listy):
    back=0
    for x in listy:
        if x>0:
            back+=x
    return back

def main():
    l1=[3,5,-4]
    if sum_positive_numbers(l1)==8:
        print("test 1 passed")
    l1 = [-4]
    if sum_positive_numbers(l1) == 0:
        print("test 2 passed")
    l1 = []
    if sum_positive_numbers(l1) == 0:
        print("test 3 passed")
    l1 = [3]
    if sum_positive_numbers(l1) == 3:
        print("test 4 passed")
if __name__=='__main__':
    main()