


def number_of_instances_helper(number_list, size):
    if size==0:
        return 0
    else:
        if number_list[size-1]==42:
            return 1 + number_of_instances_helper(number_list, size-1)
        else:
            return number_of_instances_helper(number_list, size-1)


def number_of_instances(number_list):
    return number_of_instances_helper(number_list,len(number_list))
listy=[42,4,3,2,42,1,42,42,1]
print(number_of_instances(listy))