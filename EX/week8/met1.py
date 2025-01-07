def check_dig(number,dig):
    counter=0
    while number>0:
        if number%10==dig:
            counter+=1
        number//=10
    return counter

#print(check_dig(1242,2))


def find_common_dig(number):
    max_dig=0
    count_max=0
    for dig in range(10):
        count=check_dig(number,dig)
        if count>count_max:
            max_dig=dig
            count_max=count
    return max_dig


def find_common_dig_with_count(number):
    dig_list=[0]*10
    while number>0:
        dig=number%10
        dig_list[dig]+=1
        number//=10
    find_max_number_in_list(dig_list)



def main():
    number=121311131131# int(input("Number "))
    result=find_common_dig(number)
    result1=find_common_dig_with_count(result)
    print(result)

if __name__ == '__main__':
    main()