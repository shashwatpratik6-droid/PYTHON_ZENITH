x = int(input())
y = int(input())

m = max(x,y)
div = m
while div<(x*y):
    if x%div==0 and y%div==0:
        lcm=div
        break
    div+=1

