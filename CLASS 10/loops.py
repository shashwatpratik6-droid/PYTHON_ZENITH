n = int(input())
sum = 0
while n>0:
    d = n%10
    sum = sum*10 +d
    n = n//10
print(sum)
