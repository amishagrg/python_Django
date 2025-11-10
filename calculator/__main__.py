from add import add_numbers
from subtract import subtract_numbers

if __name__ == "__main__":
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")

    choice = input("Enter 1 or 2: ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == "1":
        print("Result:", add_numbers(num1, num2))
    elif choice == "2":
        print("Result:", subtract_numbers(num1, num2))
    else:
        print("Invalid choice!")
