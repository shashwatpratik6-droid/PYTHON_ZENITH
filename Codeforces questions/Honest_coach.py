x = int(input())

for i in range(x):
    y = int(input())
    a = list(map(int, input().split()))
    a.sort()

    ans = a[1] - a[0]

    for k in range(1, y - 1):
        diff = a[k + 1] - a[k]
        if diff < ans:
            ans = diff

    print(ans)

