matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rows = len(matrix)
cols = len(matrix[0])

for d in range(rows + cols - 1):
    for i in range(rows):
        j = d - i

        if 0 <= j < cols:
            print(matrix[i][j], end=" ")