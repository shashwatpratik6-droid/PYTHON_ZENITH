# def greet(name,lala):
#     print("Hello", name)
# greet("john", "lala")


# def greet():
#     print("Hello")


# greet
# greet()

def square(n):
    return n*n

def cube(n):
    return n*n*n

tollbox = [square,cube]

print(tollbox[0](5))
print(tollbox[1](5))