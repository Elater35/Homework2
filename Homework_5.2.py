# Модифікація калькулятора.

while True:

    further_actions_1 = "Do you want the mathematical operations? "
    further_actions_2 = "Enter ('y' or 'yes') in case of consent "
    further_actions_3 = "or ('n' or 'no') to exit the program: "

    further_actions = input(further_actions_1+further_actions_2+further_actions_3)

    if further_actions.lower() not in ("y", "yes", "n", "no"):
        print("Error. Enter the correct answer.")

    elif further_actions.lower() in ("n", "no"):
        break

    elif further_actions.lower() in ("y", "yes"):

        number_1 = int(input("Enter the first number of the mathematical operation: "))
        number_2 = int(input("Enter the second number of the mathematical operation: "))
        math_operation = input("Enter the action of the mathematical operation: +, -, * or /: ")

        if math_operation not in ("+", "-", "*", "/"):
            print("Error. Incorrect action.")

        elif math_operation == "+":
            print(number_1, "+", number_2, "=", number_1 + number_2)
        elif math_operation == "-":
            print(number_1, "-", number_2, "=", number_1 - number_2)
        elif math_operation == "*":
            print(number_1, "*", number_2, "=", number_1 * number_2)

        elif number_2 == 0:
            print("Error. Numbers are not divisible by zero.")
        else:
            print(number_1, "/", number_2, "=", number_1 / number_2)
