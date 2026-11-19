matrix = [[1,2,3],[4,5,6]]
result = [[0]*len(matrix) for _ in range(len(matrix[0]))]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end="")
    print()
print("="*10)
for i in range(len(result)):
    for j in range(len(result[i])):
        result[i][j] = matrix[j][i]
        print(result[i][j],end="")
    print()