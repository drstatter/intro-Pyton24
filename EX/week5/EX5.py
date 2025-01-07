base=4
output=""
for raw in range(1,base+1):
    #space
    for i in range(base-raw):
        output+="$"
    #star
    for i in range(raw):
        output+="*"
    output+="\n"
print(output)