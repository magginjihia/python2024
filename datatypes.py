a = 3
b = 45.8
c = "emobilis"
d = True
e = False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

str = "Welcome to coding"
str2 = " at emobilis Training institute"
print(str[0:4])
print(str[5])
print(str + str2)  #concatenation
majina = ["Erick", "Mercy", "John", "Purity", "Joy"]  #list datatype - can change values(mutable)
print(type(majina))
majina[0] = "Emmanuel"
print(f"my name is {majina[0]}")

matunda = ("Banana", "mangoes", "pineapples", "Oranges")  #tuple datatype - cannot change the value(unmutable)
print(f"I like eating {matunda[2]}")
print(type(matunda))
# matunda[2] = "Watermelon"

#set datatype - has no index. it's unordered

magari = {"Toyota", "Nissan", "Honda", "Mazda", "Mercedes"}
print(f"I drive a Toyota")
print(type(magari))

print(majina)
print(matunda)
print(magari)

# dictionary data structure
mydict = {"Age": 20, "salary": 100000, "gender": "male", "name": "john"}
print(type(mydict))
print(f"The age of the employee is {mydict['Age']}")
print(f"The salary of the employee is {mydict['salary']}")
print(f"The gender of the employee is {mydict['gender']}")
print(f"The name of the employee is {mydict['name']}")