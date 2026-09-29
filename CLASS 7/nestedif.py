age = int(input())
income = int(input())
if age>18:
    if income>75000:
        print("loan approvied")
        if income>100000:
            print("Rich Guy")
        else:
            print("Middle class")
    else:
        print("loan not approvied")
else:
    print("Not elligible")