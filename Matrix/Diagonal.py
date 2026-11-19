matrix  = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (i+j)==len(matrix)-1:
            print(matrix[i][j],end="")
        else:
            print("#",end="")
    print()