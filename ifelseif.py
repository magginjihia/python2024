mark = int(input("Enter Marks:"))
# num = int(input("enter the first "))
# if num1>num 2,  is the largest number
if mark >= 80 and mark <= 100:
    print("You have an A")
elif mark >= 60 and mark <= 79:
    print("You have a B")
elif mark >= 40 and mark <= 59:
    print("You have a C")
elif mark >= 0 and mark <= 39:
    print("You have failed terribly")
else:
    print("wrong input, Check your marks")
