n = int(input())

if n < 0:
    print("false")
else:
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
        
    if original == reversed_num:
        print("true")
    else:
        print("false")