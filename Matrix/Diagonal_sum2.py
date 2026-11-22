matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i+j == len(matrix)-1 :
            sum+=matrix[i][j]
        else:
            continue
print(sum)