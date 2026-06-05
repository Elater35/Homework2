# Перемістити останній елемент списку з кінця на початок.

input_lst = [12, 3, 4, 10, 8]
print(input_lst)

if len(input_lst) > 1:
    input_lst.insert(0, input_lst[-1])
    input_lst.pop()

print(input_lst)
