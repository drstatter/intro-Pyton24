def is_sorted_list(my_list):
    pre_num=my_list[0]
    for num in my_list:
        if num < pre_num:
            return False
        pre_num=num
    return True
# my tests
#print(is_sorted_list([1,2,5]))
def main():
    my_list = [4]
    print(is_sorted_list(my_list))  # True
    my_list = [5, 4, 3, 2, 1]
    print(is_sorted_list(my_list))  # false
    my_list = [1, 12, 3, 3, 6]
    print(is_sorted_list(my_list))  # False
if __name__ == '__main__':
    main()