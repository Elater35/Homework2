# Діапазон букв.

import string
print(string.ascii_letters)

input_str = input("Enter two letters, including uppercase, separated by a hyphen, for example, a-m, or p-D: ")

index_1 = string.ascii_letters.index(input_str[0])
index_2 = string.ascii_letters.index(input_str[2])
print(string.ascii_letters[index_1:index_2+1])
