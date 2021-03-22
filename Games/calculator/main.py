from art import logo

# Functions:
# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    should_continue = True

    while should_continue:
        for key in operations:
            print(key)

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number? "))

        answer = operations[operation_symbol](n1=num1, n2=num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        next_step = input("Type 'y' to continue calculating or 'n' to start a new session or 'e' to exit:\n").lower()

        if next_step == 'y':
            num1 = answer
        elif next_step == 'n':
            should_continue = False
            calculator()
        elif next_step == 'e':
            return print("Session is finished.")


calculator()