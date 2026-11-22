matrix = [
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, 9]
]
pos = 0
neg = 0
zeros=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]>0:
            pos+=1
        elif matrix[i][j]<0:
            neg+=1
        elif matrix[i][j]==0:
            zeros+=1
print(f"Positive: {pos}")
print(f"Negative: {neg}")
print(f"Zeros: {zeros}")