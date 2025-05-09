import random

print("Welcome to your Password Generator!")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
number_of_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("How long do you want your passwords to be? "))
print("Here are your passwords:")
for pwd in range(number_of_passwords):
    password = ""
    for p in range(password_length):
        password += random.choice(chars)
    print(password)