x = int(input())
for i in range(1,x+1):
    for s in range(0,x-i):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    for k in range(1,i):
        print("*",end="")
    print()


