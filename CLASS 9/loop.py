# i = 1
# while i<=5:
#     print(i)
#     i += 1
# print("Outside")



# N = 10
# while N>=0:
#     print(N)
#     N = N-2
# print("Outside")
# print(N)



# N = 10
# while N != 1:
#     print(N)
#     N = N-2
# print("Outside")
# print(N)

# while True:
#     password = input()
#     if password == "open_sesame":
#         print("Unlocked")
#         break
#     print("wrong, try again")


attempt=0
while True:
    pin = input()
    attempt = attempt + 1
    if pin !="5555":
        if attempt == 5:
            print("card blocked")
            break
        else:
            print("attempts left:", 5-attempt,"Try again")
