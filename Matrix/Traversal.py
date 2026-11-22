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