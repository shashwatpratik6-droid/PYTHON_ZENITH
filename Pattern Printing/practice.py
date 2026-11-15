# n = int(input())
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# x = int(input())
# for i in range(x,0,-1):
#     for s in range(0,x-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n = int(input())
# for i in range(1,n+1):
#     for s in range(n-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     for k in range(i-1,0,-1):
#         print("*",end="")

#     print()

# n = int(input())
# for i in range(n,0,-1):
#     for s in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     # for k in range(i-1,0,-1):
#     #     print("*",end="")

#     print()

n = int(input())

# Upper pyramid
for i in range(1, n+1):
    for s in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()

# Lower pyramid
for i in range(n-1, 0, -1):
    for s in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()


