i = 1
while i <= 2:
    a = 1
    while a <= i:
        b = 1
        while b <= 2:
            print("*", end="")
            b += 1
        a += 1
    print("|", end="")
    c = 1
    while c <= 3:
        print("-", end="")
        c += 1
    print()
    i += 1