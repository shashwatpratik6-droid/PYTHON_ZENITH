x = int(input())
d = []
for i in range(1,x+1):
    a,b,c = input().split()
    acronym = a[0] + b[0] + c[0]
    d.append(acronym)
for num in d:
    print(num)