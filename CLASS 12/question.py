a = int(input())
b = int(input())
n = int(input())
cnt = 0
x = 1
while x<=n:
    if x%a==0 or x%b==0:
        cnt+=1
    x+=1
print(cnt)