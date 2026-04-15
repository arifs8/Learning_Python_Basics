#You need to create a programe which will take the user input of the name, age,
#and phone number After that you need to verify if the age is greater than 18 
#he can vote and you need to print the age also in this case.

user_input = input("Enter your name: ")
print(user_input)

user_age = input("Enter your age: ")
print(user_age)

user_number = input("Enter your phone number: ")
print(user_number)

# Check if age is a valid integer using try-except
try:
    age = int(user_age)
    
    if age >= 18:
        print(f"XXXXXXXXXXXXXXXXX")
        print(f"You can vote, your age is {age}")
        print(f"Your name is {user_input}")
        print(f"Your phone number is {user_number}")
    else:
        print("You cannot vote")
except ValueError:
    print("Invalid age entered! Please enter a valid number.")
