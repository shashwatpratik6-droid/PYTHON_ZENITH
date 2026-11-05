from math import gcd
x = int(input())
list=[]
for i in range(0,x):
    a,b,k = map(int,input().split())
    g = gcd(a,b)
    dx = a//g
    dy = b//g
    if dx<=k and dy<=k:
        coins=1
    else:
        coins=2
    list.append(coins)
    i+=1
for num in list:
    print(num)