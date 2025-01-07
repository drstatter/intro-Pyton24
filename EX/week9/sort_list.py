def is_sorted_list(list_2_check):
    for i in range(len(list_2_check)-1):
        if list_2_check[i] >= list_2_check[i+1]:
            return False
    return True
def main():
    list_to_check = [0,1,2]
    print(is_sorted_list(list_to_check))
if __name__ == '__main__':
    main()