# 1. Найпростіший калькулятор. Варіант 2.

math_operation = list(input("Enter two numbers and the operation between them, for example: 4/5 or 5+12: "))

if math_operation[1] == "+":
    print(math_operation[0], "+", math_operation[2], "=", int(math_operation[0]) + int(math_operation[2]), end=" \n \n")
# elif action_math_operation == "-":
#     print(str(number1_math_operation), "-", str(number2_math_operation), "=", number1_math_operation - number2_math_operation, end=" \n \n")
# elif action_math_operation == "*":
#     print(str(number1_math_operation), "*", str(number2_math_operation), "=", number1_math_operation * number2_math_operation, end=" \n \n")
# elif number2_math_operation == 0:
#     print("Error. Numbers are not divisible by zero.", end=" \n \n")
# else:
#     print(str(number1_math_operation), "/", str(number2_math_operation), "=", number1_math_operation / number2_math_operation, end=" \n \n")
