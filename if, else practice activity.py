# simple calculator

#get user input
num1 = float(input("Enter first number"))
operation = input("Enter operation(+, -, *, /):")
num2 = float(input("Enter second number"))

#perform calculation usine if else
if operation == '+':
    result = num1 + num 2
elif operation == '-':
    result = num1 - num 2
elif operation == '*':
    result = num1 * num 2
elif operation == '/':
    result = num1 / num 2
else:
        result = "Error! Division by Zero"
else:
    result = "Error! Invalid Operation"

print(f"The result is: {result}")