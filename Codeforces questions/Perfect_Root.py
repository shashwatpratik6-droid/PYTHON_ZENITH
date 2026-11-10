x = int(input())
a = []
for i in range(1,x+1):
    y = int(input())
    a.append(y)
    i+=1

for j in range(0,len(a)):
    b = a[j]
    for k in range(1,b+1):
        print(k,"",end="")
        k+=1
    print("")
    j+=1

