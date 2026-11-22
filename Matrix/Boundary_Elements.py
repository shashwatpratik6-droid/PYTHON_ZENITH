matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
for i in range(len(matrix)):   
    for j in range(len(matrix[0])):
        if (i==0 or i==len(matrix)-1) or (j==0 or j==len(matrix[0])-1 ):
            print(matrix[i][j],end=" ")
        else :
            print(" ",end=" ")

    print()
