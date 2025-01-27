def count_dig(num):
    back_num=num
    count=0
    while back_num>0:
        if back_num%2==0:
            count=count+1
        back_num=back_num//10
    return count
def count_dig_even_rec(num):
    if num==0:
        return 0
    dig=num%10
    if dig%2==0:
        return count_dig_even_rec(num//10)+1
    else:
        return count_dig_even_rec(num//10)
def dig_in_number(num,dig):
    if num==0:
        return False
    current_digit=num%10
    if current_digit==dig:
        return True
    else:
        return dig_in_number(num//10,dig)
def reverse_print(num):
    if num==0:
        return
    print(num%10,end=" ")
    reverse_print(num//10)
def print_lad(n,all):
    if n==1:
        all.append([1])
    elif n==2:
        all.append([2])
    else:
        for l in all:
            l.append(1)
        print_lad(n-1,all)
        b=[]
        for l in all:
            temp=l.copy()
            temp.append(2)
            b.append(temp)
        all+=b
        print_lad(n-2,all)
        return all
def mod_adding(a,b):
    if a<b:
        return a
    else:
        return mod_adding(a-b,b)
def ladder(size):
    if size==2:
        return 2
    if size==1:
        return 1
    return ladder(size-1)+ladder(size-2)
print(ladder(2))
def rec_ser(num):
    if num<=3:
        return num
    else:
        if num%2==0:
           return rec_ser(num-1)+rec_ser(num-2)+rec_ser(num-3)
        else:
            return rec_ser(num-1)-rec_ser(num-3)

def rec_ser_list(num):

    listy=[0]*(num+1)
    listy[1]=1
    listy[2]=2
    listy[3]=3
    for l in range(4,num+1):
        if l%2==0:
            listy[l]=listy[l-1]+listy[l-2]+listy[l-3]
        else:
            listy[l]=listy[l-1]-listy[l-3]
    return listy[num]
def rec_ser_5pointers(num):
    save_num=num
    a=1
    b=2
    c=3
    num=num-3
    while num>0:
        num-=2
        d=a+b+c
        e=d-b
        a,b,c=c,d,e
    if num%2==0:
        return d
    else:
        return e

for i in range(4,10):
    print(rec_ser_5pointers(i),end=" ")

    #print(mod_adding(27,4))
    # print(count_dig(2342))
    # print(count_dig_even_rec(423))
    # print(dig_in_number(2342,4))
    # print(dig_in_number(2342, 5))
    # print(dig_in_number(2342, 0))
def climb_ladder(steps, path=[]):
        if steps == 0:
            print("->".join(path))
            return
        if steps >= 1:
            climb_ladder(steps - 1, path+["1"])
        if steps >= 2:
            climb_ladder(steps - 2, path + ["2"])
climb_ladder(4)
