x = int(input())
for i in range(0,x):
    y = int(input())
    for j in range(0,y):
        a = list(map(int,input().split()))
        a.sort()
        diff=0
        for k in range(0,y-1):
            difference = a[k+1]-a[k]
            diff=difference
            if difference<diff :
                ans=difference
            k+=1
        j+=1
    i+=1

