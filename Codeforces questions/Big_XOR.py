n = int(input())
arr=[]
for i in range(1,n+1):
    x = int(input())
    brr=[]
    for j in range(1,x+1):
        a=(j%2)
        brr.append(a)
    arr.append(brr)
    i+=1


for row in arr:
    print(*row)