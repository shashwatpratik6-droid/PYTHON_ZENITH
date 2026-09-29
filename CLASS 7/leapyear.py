def callender():    
    year = int(input())
    if year%4==0:
        if year%100:
            if year%400:
                print("Leap year")
            else:
                print("Not Leap year")
        else:
            print("Leap Year")
    else:
        print("Not Leap year")

    

callender()