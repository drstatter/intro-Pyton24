def sum_list_rec(num_list):
    if len(num_list)==0:
        return 0
    temp=num_list.pop(-1)
    return temp+sum_list_rec(num_list)
print(sum_list_rec([1,2,3,6]))