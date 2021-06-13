from art import logo


# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

calculation_finished = False


def calculator():
    print(logo)
    num1 = float(input("What is the first number? "))

    for i in operations:
        print(i)

    while not calculation_finished:

        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What is the next number? "))

        # which_operator = operations[operation_symbol]
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer

        choice = input(f"Type 'y' to continue calculating from {answer}, or type 'n' to start a new calculation.: ")
        if choice == "n":
            calculator()


calculator()








