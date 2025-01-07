def find_max_dig_apper_algo(num):
    save_num =num
    if num<=0:
        return 0
    dig_count=[0]*10
    while num>0:
        dig=num%10
        dig_count[dig]+=1
        num//=10
    print(dig_count,save_num)
    place=-1
    while dig_count[place]==0:
        place-=1
    return dig_count[place]

def find_max_dig_apper(num):
    num_str=str(num)
    max_dig=max(num_str)
    return num_str.count(max_dig)
find_max_dig_apper(12322)

def find_max_dig(num):
    max_dig=0
    while num>0:
        dig=num%10
        if dig>max_dig:
            max_dig=dig
        num//=10
    return max_dig

def find_max_dig_apper_simple(num):
    max_dig=find_max_dig(num)
    count=0
    while num>0:
        dig=num%10
        if dig==max_dig:
            count+=1
        num//=10
    return count





def find_max_from_2(num1,num2):
    max_val1=find_max_dig_apper(num1)
    max_val2=find_max_dig_apper(num2)
    if max_val1>max_val2:
        return num1
    else:
        return num2
def main():
    num1=13322232
    num2=9855
    print(find_max_from_2(num1,num2))

if __name__ == '__main__':
    main()
