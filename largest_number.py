num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))
num3 = int(input("Enter third Number: "))
num4 = int(input("Enter fourth Number: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"{num1} is the greatest number")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"{num2} is the greatest number")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"{num3} is the greatest number")
elif num4 > num1 and num4 > num2 and num4 > num3:
    print(f"{num4} is the greatest number")
else:
    print("The numbers are all equal")

if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"{num1} is greater than {num2, num3, num4}")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"{num2} is greater than {num1, num3, num4}")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"{num1} is greater than {num2, num3, num4}")
elif num4 > num1 and num4 > num2 and num4 > num3:
    print(f"{num4} is the greatest number")
else:
    print("The numbers are all equal")
