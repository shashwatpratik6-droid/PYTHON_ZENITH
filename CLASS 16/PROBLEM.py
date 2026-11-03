m = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
R = len(m)
i = 0
main = 0
anti = 0
while i<R:
    main += m[i][i]
    anti += m[i][R - 1 - i]
    i += 1

print(main,anti)