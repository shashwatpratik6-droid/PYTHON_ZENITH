def student(name,age,city):
    print(name)
    print(age)
    print(city)
# student(age=21,name="Rahul",city="Delhi")
# student(age=21,city="Delhi",name="Rahul")
student("Rahul",age=21,city="karnatka")
# No duplicate values are allowed in the argument like age

print("Hello","Students","Python",sep="|")

# print("Hello",end="\n")
print("Hello",end=" ")
print("World")

nums = [1,2,3,4,6,7]
print(sorted(nums,reverse=False))


def greet(name,greet="Good Morning!"):
    print(name,greet)
greet("Shahswat")
greet("Shashwat","Good Night!")


# Args and Kwargs

def total(*nums):
    print(type(nums))
    s=0
    for n in nums:
        s+=n
    print(s)

total(5,4,6,5,4)

