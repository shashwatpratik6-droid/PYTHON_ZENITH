x = int(input())
l = []
for i in range(1,x+1):
    h,m = map(int,input().split())
    if h<=23 and m==0:
        n = (24-h)*60 
    elif h<=23 and m!=0:
        d = (23-h)*60
        e = 60-m
        n = d+e
    l.append(n)
    i+=1
for j in range(0,len(l)):
    print(l[j])
    j+=1