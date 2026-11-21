n = int(input())
for i in range(1,n+1):
    if i%2==0:
        for j in range(n*i,(n*i-(n-1))-1,-1):
            print(j,end="")
    elif i%2!=0:
        for j in range(n*i-(n-1),(n*i)+1):
            print(j,end="")
        print()


# n = int(input())
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         for j in range(n * i, (n * i - (n - 1)) - 1, -1):
#             print(j, end=" ")
#     elif i % 2 != 0:
#         for j in range(n * i - (n - 1), (n * i) + 1):
#             print(j, end=" ")
#     print()