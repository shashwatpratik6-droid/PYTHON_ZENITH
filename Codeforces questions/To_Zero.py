x = int(input())
d = []
for i in range(1,x+1):
    n,k = map(int,input().split())
    if n%2==0:
        c = k-1
        a = (n + c - 1) // c
        d.append(a)
    else:
        n = (n-k)
        b = (n + (k - 2)) // (k - 1)
        d.append(b+1)

for num in d:
    print(num)