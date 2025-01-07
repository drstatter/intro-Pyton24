def find_max_list(listy):
    if len(listy) == 0:
        return None
    max_val = listy[0]
    for num in listy:
        if num > max_val:
            max_val = num
    return max_val

def find_max_index_list(listy):
    if len(listy) == 0:
        return None
    max_index = 0
    for i in range(1, len(listy)):
        if listy[i] > listy[max_index]:
            max_index = i
    return max_index

def main():
    my_list=[4,3,42,7,9,100,3,45]
    index=find_max_index_list(my_list)
    print(f"Maximum value: in {index} and it is {my_list[index]}")
if __name__ == "__main__":
    main()