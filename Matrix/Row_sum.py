matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i==1:
            sum+=matrix[i][j]

print(sum)

## Also we can use this form of code

i = 0
total = 0

while i < len(matrix[1]):
    total += matrix[1][i]
    i += 1

print(total)