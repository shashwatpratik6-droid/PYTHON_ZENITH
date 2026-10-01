# # Write your reference solution here
# n = int(input())
# if( n>0 and n%2==0 and n>100):
#     print("Positive")
#     print("Even")
#     print("Large")
# elif (n<0 and n%2==0 and n<100):
#     print("Even")
# elif  (n>0 and n%2!=0 and n<100):
#     print("Positive")
# else:
#     print("Nothing")

# Write your reference solution here
score = int(input())
attendance = int(input())
if(score>=90 and attendance>=90):
    print("Star Student")
    print("Perfect Attendance")
elif(score>=90 and attendance<90):
    print("Star Student")
else:
    print("No badges earned.")    