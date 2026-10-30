n = int(input())
i = 1
while i<=n:
    print(" "*(n-i),end="")
    j = i
    while j>=1:
        print(j,end="")
        j-=1
    print()
    i+=1
