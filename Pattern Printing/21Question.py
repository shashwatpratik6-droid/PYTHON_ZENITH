n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2==0  and j%2!=0:
            print(" ",end=" ")
        elif i%2==0  and j%2==0:
            print("*",end=" ")
        elif i%2!=0  and j%2==0:
            print(" ",end=" ")
        elif i%2!=0  and j%2!=0:
            print("*",end=" ")
    print()
for i in range(n,1,-1):
    for k in range(1,i):
        if i%2!=0  and k%2!=0:
            print(" ",end=" ")
        elif i%2!=0  and k%2==0:
            print("*",end=" ")
        elif i%2==0  and k%2==0:
            print(" ",end=" ")
        elif i%2==0  and k%2!=0:
            print("*",end=" ")
    print()