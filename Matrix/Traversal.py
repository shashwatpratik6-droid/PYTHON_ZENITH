matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
row = len(matrix)
col = len(matrix[0])
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
row = len(matrix)
col = len(matrix[0])
for i in range(row-1):
    print(matrix[0][i],end=" ")
for j in range(col-1):
    print(matrix[j][col-1],end=" ")
for j in range(col-1,-1,-1):
    print(matrix[col-1][j],end=" ")
for i in range(row-2,-1,-1):
    print(matrix[i][0],end=" ")



