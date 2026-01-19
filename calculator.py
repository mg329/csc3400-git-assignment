import math
def calculator():
    statement = True
    while statement:
        num1 = float(input())
        operator = input()
        if operator == "square root":
            result = squareRoot(num1)
        else:
            num2 = float(input())
            result = calculate(num1, num2, operator)

        if result == -1:
            print("Cannot divide by zero")
        elif result == -2:
            print("Invalid operator")
        elif result == -3:
            print("Cannot take square root of negative value")
        else:
            print("Result: ", result)
        
        question = input("Do another calculation? (yes/no): ").lower()

        if question == "no" or question == "n":
            statement = False

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return -1
        return num1 / num2
    elif operator == "^":
        return num1 ** num2
    else:
        return -2
    
def squareRoot(num1):
    if num1 < 0:
        return -3
    return math.sqrt(num1)
    

if __name__ == "__main__":
    calculator()