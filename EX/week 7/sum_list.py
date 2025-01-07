my_list=[7,4,3,5,6,7,8,9,10]
def sum_in_list(data_list):
    sum_of_3=0
    for num in data_list:
        if num%3==0:
            sum_of_3+=num
    return sum_of_3
print(sum_in_list(my_list))

