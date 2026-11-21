n = int(input())
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for i in range(n,1,-1):
    for d in range(n-i+2,1,-1):
        print(" ",end="")
    for k in range(i,1,-1):
        print("*",end=" ")
    print()