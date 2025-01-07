# st="   *\n"+"  **\n"+" ***\n"+"****\n"+" ***\n"+"  **\n"+"   *\n"
# my_output="\n"
# base=4
# for row in range(1,base+1):
#     #space
#     for _ in range(base-row):
#         my_output+=" "
#     # print star
#     for j in range(row):
#         my_output+="*"
#     my_output+="\n"
# #lower triangle
# for row in range(base-1,0,-1):
#     #space
#     for _ in range(base-row):
#         my_output+=" "
#     # print star
#     for j in range(row):
#         my_output+="*"
#     my_output+="\n"
# #print(my_output)
#
base=4
my_output=""
for row in range(1,base+1):
    my_output+=" "*(base-row)+"*"*row+"\n"
print(my_output)
# if my_output==st:
#       print(my_output)