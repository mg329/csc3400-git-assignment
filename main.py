from calculator import add, subtract, multiply, divide, power, square_root

def main():
    again = True
    
    while again:
        print("\nSelect Operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Square Root\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == "7":
            print("Thank you for using the calculator.")
            again = False
        elif choice == "1":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid number input.")
            result = add(a, b)
            print("Result: ", result)
        elif choice == "2":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid number input.")
            result = subtract(a, b)
            print("Result: ", result)
        elif choice == "3":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid number input.")
            result = multiply(a, b)
            print("Result: ", result)
        elif choice == "4":
            try:
                try:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid number input.")
            except ValueError as e:
                print("Error: ", e)
                continue
            result = divide(a, b)
            print("Result: ", result)
        elif choice == "5":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid number input.")
            result = power(a, b)
            print("Result: ", result)
        elif choice == "6":
            try:
                try:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid number input.")
            except ValueError as e:
                print("Error: ", e)
                continue
            result = divide(a, b)
            print("Result: ", result)
        else:
            print("Invalid choice. Try again")

if __name__ == "__main__":
    main()