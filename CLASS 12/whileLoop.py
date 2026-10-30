x = int(input())
y = int(input())

limit = min(x,y)
div = limit
while div>0:
    if x%div==0 and y%div==0:
        gcd=div
        break
    div-=1
print(gcd)
    