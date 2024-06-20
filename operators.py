# arithmetic operators
x = 36
y = 6

print(f"Addition operator {x + y}")
print(f"Subtraction operator {x - y}")
print(f"multiplication operator {x * y}")
print(f"Division operator {x / y}")
print(f"Remainder operator {x % y}")

#comparison operator
print(f"{x} is not equal to {y}:", x != y)
print(f"{x} is equal to {y}:", x == y)
print(f"is {x} greater than {y}:", x > y)
print(f"is {x} less than {y}:", x < y)
print(f"is {x} greater than or equals to {y}:", x >= y)
print(f"is {x} less than or equals to {y}:", x <= y)

#logical operators
print("is this statement true?:", x > y and x < y)
print("is this statement true?:", x > y or x < y)
print("Each statement is true then return false and vice versa:", (not(x > y and x < y)))