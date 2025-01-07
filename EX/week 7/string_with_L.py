word="L534543L^^%$&"
l_sum=0
for char in word:
    if char=="L":
        l_sum+=1
print(l_sum)
print(word.count("L"))
word.casefold()