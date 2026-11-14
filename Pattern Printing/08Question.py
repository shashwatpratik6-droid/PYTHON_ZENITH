x = int(input())
for i in range(0,x):
    for s in range(0,i):
        print(" ",end="")
    for j in range(0,x-i):
        print("*",end="")
    print()