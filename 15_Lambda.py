user_input  = input("Enter your name: ")
print(user_input)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")

if user_input == "Syeda":
    print("Hello, Syeda!")
else:
    print("Hello, " + user_input)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")

user_input2 = input("Enter your age: ")
print(user_input2)  

age = int(user_input2)

if age >=18:
    print("Adult")
else:
    print("Minor")

#Lambda Functions

result = lambda age : "Adult" if age >= 18 else "Minor"
print(result(age))