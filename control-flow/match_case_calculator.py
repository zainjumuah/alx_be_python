# Get user input
user_input1 = input("Enter the first number: ")
user_input2 = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")

#Tryna catch some sneaky errors here
try:
    num1 = float(user_input1)
    num2 = float(user_input2)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

# Match-Case statement that performs the ops based on the string input    
match operation:
    case '+':
        op_result = num1 + num2
    case '-':
        op_result = num1 - num2 
    case '*':
        op_result = num1 * num2
    case '/':
        if num2 != 0:
            op_result = num1 / num2
    case _:
        op_result = "Invalid operation, carry your matter dey go abeggiiii"

print(f"The result is {op_result}" if num2 != 0 and operation == '/' else "Cannot divide by zero.")
