def find_sep(word):
    index =0
    back=list()
    count=0
    while index < len(word):
        char = word[index]
        if not(char=="!" or char =="."):
             count+=1
             index+=1
        else:
            #new sentence
            back.append(count)
            count=0
            index+=1
            while index < len(word) and word[index]==" ":
                index+=1
    return back

print(find_sep("Hi! This is a lovely day. Please join me for breakfast!"))
print(find_sep("Hi! This is a lovely day. Please join me for breakfast"))
print(find_sep("Hi  ! This is a lovely day.     Please    join me for breakfast!"))