x = int(input())
for i in range(1,x+1):
    for s in range(0,x-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(i,end="")
    print()