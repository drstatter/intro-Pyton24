def cut_str(word):
    index=0
    back=[]
    while index<len(word):
        if word[index]==" ":
            index+=1
        else:
            count=0
            while index<len(word) and not(word[index]=="." or word[index]=="!"):
                count+=1
                index+=1
            if index<len(word):
                back.append(count)
                index+=1
    return back

print(cut_str("   hi. 3hjkhkj4!34"))