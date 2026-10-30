n = int(input())
current = n%10
n = n//10
increasing = True
while n>0:
    d = n%10
    if d>=current:
        increasing = False
        break
    current = d
    n = n//10
if increasing:
    print("Yes")
else:
    print("No")