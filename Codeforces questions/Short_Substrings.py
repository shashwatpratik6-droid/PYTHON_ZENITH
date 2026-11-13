x = int(input())
l = []
for i in range(1,x+1):
    d = []
    string=input()
    d.append(string[0])

    j = 1
    while j<len(string):
            c = string[j]
            d.append(c)
            j+=2
    l.append(d)
    i+=1
    
for val in l:
    for Val in val:
        print (Val,end="")
    print()
    