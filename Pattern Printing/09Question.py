x = int(input())
for i in range(x,0,-1):
    for s in range(x-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()