INTERSCTION=1
UNION=2
DEFSET=3
def find_elements(list1,list2,par):
    set1 = set(list1)
    set2 = set(list2)
    if par==INTERSCTION:
        back=set()
        for element in set1:
            if element in set2:
                back.add(element)
    if par==UNION:
        return set1 | set2
    if par==DEFSET:
        return set1-set2
