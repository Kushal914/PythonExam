num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

try:
    ans = num1 / num2
    print(f"{num1} / {num2} = {ans}")
except Exception as e:
    print(e)