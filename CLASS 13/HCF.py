x = int(input())
y = int(input())

limit = min(x,y)
i=limit
gcd=0
while i>0:
    if x%i==0 and y%i==0:
        gcd=i
        break
    i-=1
print(gcd)