num1 = 3
print(num1)
print(id(num1))
print(type(num1))
print(id(3))
num2 = 3
print(num2)
print(id(num2))
print(type(num2))

print(num1 == num2)
print(num1 is num2)

num2 = (3,)
print(type(num2))
print(id(num2))
print(num1 == num2)
print(num1 is num2)