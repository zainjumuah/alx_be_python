
def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation: add, subtract, multiply, or divide.
    Returns the result, or a message if division by zero is attempted.
    """

    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2
        case _:
            return "Error: Invalid operation"
