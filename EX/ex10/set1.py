INTERCTION=1
UNION=2
SUBSET=3
def check_lists(list1,list2,what_2_do):
    set1 = set(list1)
    set2 = set(list2)
    if what_2_do==INTERCTION:
        return set1 & set2
    if what_2_do==UNION:
        return set1 | set2
    if what_2_do==SUBSET:
        return set1 - set2

list1 = [1,2,3,4,5]
list2 = [2,4,6,8]
print(check_lists(list1,list2,INTERCTION))
print(check_lists(list1,list2,UNION))
print(check_lists(list1,list2,SUBSET))
