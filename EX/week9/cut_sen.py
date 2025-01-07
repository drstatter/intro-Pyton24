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
def cut_str_for(word):
    back=list()
    count=0
    for char in word:
        if not(char==" " and count==0):
            if char=="!" or char==".":
                back.append(count)
                count=0
            else:
                count+=1
    return back
print(cut_str_for("   hi. 3hjkhkj4!3 4!"))