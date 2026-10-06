# year = int(input())

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not Leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not Leap year")

n = int(input("Enter a year: "))

if n%400==0 or (n%4==0 and n%100!=0):
    print("leap")
else:
    print("not leap")