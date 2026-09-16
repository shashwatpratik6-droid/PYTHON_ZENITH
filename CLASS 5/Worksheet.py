Write your reference solution here
a = int(input())
b = int(input())
c = int(input())
s = (a + b + c) / 2
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
print(area)



print(True == 1)
print(False == 0)
print(True + True)
print(False + 5)



print(0 or 5)
print("" or "hi")
print(3 and 7 and 10 and "" and "tom")
print(0 and 7)


tittle= input("enter your name: ")
mid name= input("enter mid name: ")
last name= input("enter last name: ")
if(tittle==""):
    print("Mr")
elif(midname=""):
    print("Zen")
elif(lastname=""):
    print("G")
else:
    print(tittle,mid name,last name)



tittle= input() or "Mr"

Midname= input() or "Zen"

Lastname= input() or "G"
print(tittle,Midname,Lastname)


x = 8
y = ""
print(not y or x and y or not x)