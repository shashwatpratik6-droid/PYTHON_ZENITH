matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i==j:
            Sum+=matrix[i][j]
        else:
            continue

print(Sum)