matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for j in range(len(matrix[0])):
    total = 0
    for i in range(len(matrix)):
        total+=matrix[i][j]
    print(total)