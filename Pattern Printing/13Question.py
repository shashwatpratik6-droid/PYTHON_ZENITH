x = int(input())
for i in range(0,x):
    for s in range(0,x-i):
        print(" ",end="")
    if i <(x-1):
        for j in range(0,1):
            print("*",end="")
    if i>0 and i<(x-1):
        print(" "*(2*i-1)+"*",end="")
    if i==(x-1):
        print("*"*((2*i)+1))
    print()