print("CALCULATOR")

def calculate():
    """Performs a calculation based on user input."""
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /, %): ")

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            return 
        else:
            result = num1 / num2
    elif op == '%':
        result = num1 % num2
    else:
        print("Invalid operator.")
        return 

    if num1.is_integer() and num2.is_integer():
        print(int(result))
    else:
        print(result)

while True:
    calculate()
    choice = input("Perform another calculation? (yes/no): ").lower()
    if choice != 'yes':
        print("Exited") 
        break 


