mat=[[4,3,2,1],[7,5,3,1]]
def print_mat(my_mat):
    for row in my_mat:
        for num in row:
            print(num, end=" ")
        print()
print_mat(mat)