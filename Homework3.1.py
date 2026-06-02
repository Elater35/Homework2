# 1. Найпростіший калькулятор.

number1_math_operation = int(input("Enter the first number of the mathematical operation: "))
number2_math_operation = int(input("Enter the second number of the mathematical operation: "))
action_math_operation = input("Enter the action of the mathematical operation: +, -, * or /: ")

if action_math_operation != "+" and action_math_operation != "-" and action_math_operation != "*" and action_math_operation != "/":
    print("Error. Incorrect action.")

elif action_math_operation == "+":
    print(str(number1_math_operation), "+", str(number2_math_operation), "=", number1_math_operation + number2_math_operation)
elif action_math_operation == "-":
    print(str(number1_math_operation), "-", str(number2_math_operation), "=", number1_math_operation - number2_math_operation)
elif action_math_operation == "*":
    print(str(number1_math_operation), "*", str(number2_math_operation), "=", number1_math_operation * number2_math_operation)

elif number2_math_operation == 0:
    print("Error. Numbers are not divisible by zero.")
else:
    print(str(number1_math_operation), "/", str(number2_math_operation), "=", number1_math_operation / number2_math_operation)
