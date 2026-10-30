x = int(input())
y = int(input())

i = max(x,y)
lcm=0
a= (x*y)
while i<x:
    if x%i==0 and y%i==0:
        lcm=i
        break
    lcm+=1
print(lcm)