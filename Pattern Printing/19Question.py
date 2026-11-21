n = int(input())
for i in range(1,n+1):
    for s in range(1,i):
        print(" ",end="")
    for j in range(0,n):
        print("*",end="")
    print()   