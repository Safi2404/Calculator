# Menu Driven Calculator

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def mod(a, b):
    if b == 0:
        return "Error! Modulus by zero."
    return a % b

while True:
    print("\n----- CALCULATOR MENU -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus (%)")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "6":
        print("Exiting the program...")
        break

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice! Please try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))

    elif choice == "2":
        print("Result:", sub(num1, num2))

    elif choice == "3":
        print("Result:", mul(num1, num2))

    elif choice == "4":
        print("Result:", div(num1, num2))

    elif choice == "5":
        print("Result:", mod(num1, num2))
