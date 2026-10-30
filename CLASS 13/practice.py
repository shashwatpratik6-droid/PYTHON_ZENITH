a,b=map(int,input().split())
i = min(a,b)
gcd = 0
while i>0:
    if a%i==0 and b%i==0:
        gcd=i
    i-=1
print(gcd)