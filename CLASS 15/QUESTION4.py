n = int(input())
i = 1
while i<=n:
    print(" "*(n-i),end="")
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1

