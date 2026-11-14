row = int(input())
for i in range(row,0,-1):
    for s in range(row-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(i,end="")
    print()
