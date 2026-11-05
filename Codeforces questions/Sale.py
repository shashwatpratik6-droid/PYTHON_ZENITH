m,n = map(int,input().split())
x = min(m,n)
y = max(m,n)
a = list(map(int,input().split()))
a.sort()
sum = 0
for i in range(0,x):
    c=0
    c=a[i]
    if c>=0 :
        break
    sum+=c
print(abs(sum))