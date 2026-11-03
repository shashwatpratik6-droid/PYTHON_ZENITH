n = int(input())
arr=[]
for i in range(1,n+1):
    x,y = map(int,input().split())
    a=(y-x)
    arr.append(a)
    i+=1
for num in arr:
    print(num)