def number_checking():
    if num1.isnumeric() and num2.isnumeric():
        return True

requestedOperation = input("Enter the operation you want to perform: ").lower()
if requestedOperation == "add":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    number_checking
    print(f"The result is: {num1 + num2}")
elif requestedOperation == "subtract":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    number_checking()
    print(f"The result is: {num1 - num2}")
elif requestedOperation == "multiply":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    number_checking()
    print(f"The result is: {num1 * num2}")
elif requestedOperation == "divide":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    number_checking()
    print(f"The result is: {num1 / num2}")
else:
    print("Invalid operation")