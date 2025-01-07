

def compare_num_by_max_fer(listy):
    max_val=-1
    max_fer=0
    for num in listy:
        val=find_max_fer_str(num)
        if val>max_fer:
            max_fer=val
            max_val=num
        return max_val

def find_max_fer(num):
    dig_count=[0]*10
    while num>0:
        dig=num%10
        dig_count[dig]+=1
        num//=10
    index=-1
    while dig_count[index]==0:
        index-=1
    return dig_count[index]
find_max_fer(1128999)

def find_max_fer_str(num):
    num_str=str(num)
    max_dig=max(num_str)
    return num_str.count(max_dig)


def find_max_fer_simple(num):
    max_dig=find_max_dig(num)
    count=0
    while num>0:
        dig=num%10
        if dig==max_dig:
            count+=1
        num//=10
    return count
print(find_max_fer(123239991))

def find_max_dig(num):
    max_dig=0
    while num>0:
        dig=num%10
        if dig>max_dig:
            max_dig=dig
        num//=10
    return max_dig
#print(find_max_dig((122214111)))
def main():
    num1=1332232
    num2=9855
    listy=[num1,num2,12328]
    print(compare_num_by_max_fer(listy))
if __name__ == '__main__':
    main()