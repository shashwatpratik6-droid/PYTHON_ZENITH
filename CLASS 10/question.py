n = int(input())
temp=n
count_digit=0
while n>0:
    count_digit +=  1
    n = n//10
sum = 0
n = temp
while temp>0:
    d = temp%10
    sum=sum+d**count_digit
    temp = temp//10

if sum==n:
    print("Yes")
else:
    print("No")
