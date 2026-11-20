matrix = [
    [12, 45, 23],
    [67, 11, 89],
    [34, 56, 78]
]
largest_num = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if largest_num<matrix[i][j]:
            largest_num = matrix[i][j]
        else:
            continue

print(largest_num)
            