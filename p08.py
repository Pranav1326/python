# Python program of input type of String, Integer and Array
# By : Pranav Visavadia

name = input("Enter Your name: ")
age = int(input("Enter you age: "))

hobbies = []
n = int(input("Enter no of hobbies: "))

for i in range(0, n):
    element = input("Enter Hobby: ")
    
    hobbies.append(element)

print("Hello," + name)
print("Your age is", age)
print(hobbies)
