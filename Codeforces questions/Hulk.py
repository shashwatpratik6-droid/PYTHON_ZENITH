n = int(input())
for i in range(1,n+1):
    if i%2==0 and i<n:
        print("I love that ",end="")
    if i%2!=0 and i<n:
        print("I hate that ",end="")
    if i%2==0 and i==n:
        print("I love it",end="")
    if i%2!=0 and i==n:
        print("I hate it",end="")
    i+=1


# I hate that I love it