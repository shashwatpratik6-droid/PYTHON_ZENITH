matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
count=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]%2!=0:
            count+=1

print(count)