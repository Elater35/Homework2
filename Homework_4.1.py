# Перемістити всі нулі до кінця списку.

# input_lst = []
# input_lst = [0]
# input_lst = [2, 0, 0, 16, 0, 3, 27, 0, 5, 318, 7, 55, 9]
# input_lst = [2, 16, 3, 27, 5, 318, 7, 55, 9]

input_lst = [0, 2, 16, 0, 3, 27, 0, 5, 318, 7, 55, 9, 0, 0, 0, 0, 0]

print(input_lst)

number_zeros_of_lst = input_lst.count(0)
# print(number_zeros_of_lst)

length_lst = len(input_lst)
# print(length_lst)

cycle_counter = 0

while cycle_counter < number_zeros_of_lst:
    index_zero = input_lst.index(0)
    # print(index_zero)

    if index_zero == length_lst - number_zeros_of_lst: # якщо решта нулів вже в кінці списку, виходимо з циклу
        break

    input_lst.insert(length_lst+1,0)
    input_lst.pop(index_zero)

    cycle_counter += 1

print(input_lst)
