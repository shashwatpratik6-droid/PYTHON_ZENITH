n = int(input())
l = []
for i in range(0,n):
    a,b,c,d = map(int,input().split())
    count = 0
    if a>b:
        for j in range(b,a+1):
            if c==j or d==j:
                count += 1
        if count == 1:
            answer = "YES"
        else:
            answer = "NO"
        l.append(answer)
    elif a<b:
        for j in range(a,b+1):
            if c==j or d==j:
                count += 1
        if count == 1:
            answer = "YES"
        else:
            answer = "NO"
        l.append(answer)

for val in l:
    print(val)