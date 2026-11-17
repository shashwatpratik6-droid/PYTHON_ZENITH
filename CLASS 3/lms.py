n = int(input())
i = 0
sum = 0
while True:
        while n>0:
                x = n%10
                sum+=x
                n = n//10
        if sum>=10 :
                while n>0:
                        x = n%10
                        sum+=x
                        n = n//10
        else:
                break
        i+=1
print(i)