# Чи може рядок бути ім'ям змінної.

import string
import keyword
print(keyword.kwlist)
print(string.punctuation)

input_str = ""

while input_str == "":
    input_str = input("Enter non-empty string: ")

print(input_str)

index_ = 0

if input_str[0].isdigit() or (input_str in keyword.kwlist) or ("__" in input_str):
    print("False. This string cannot be a variable name.")

else:
    for item_1 in input_str:
        if 65 <= ord(item_1) <= 90 or item_1 == " " or (item_1 in string.punctuation and item_1 != "_"):
            print("False. This string cannot be a variable name.")
            break
        index_ += +1

if index_ == len(input_str):
    print("True. Valid variable name.")
