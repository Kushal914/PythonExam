name = input("Enter your name: ")
age = int(input("Enter your age: "))

info = f"Name: {name}, Age: {age}"

with open('info.txt', 'a') as file:
    file.write(info + '\n')