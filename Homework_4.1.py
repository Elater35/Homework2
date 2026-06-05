# Перемістити всі нулі до кінця списку.

input_lst = [2, 0, 0, 16, 0, 3, 27, 0, 5, 318, 7, 55, 9, 0]
print(input_lst)
# input_lst = [2, 16, 3, 27, 5, 318, 7, 55, 9]
# input_lst = [2, 16, 3, 27, 0, 5, 318, 7, 55, 9, 0, 0, 0, 0, 0]

number_zeros_of_lst = input_lst.count(0)
print(number_zeros_of_lst)
cycle_counter = 0

# for cycle_counter == 0
while cycle_counter < number_zeros_of_lst:
    ind = input_lst.index(0)
    if ind == len(input_lst) - number_zeros_of_lst:
        break
    input_lst.insert(-1,0)
    input_lst.pop(number_zeros_of_lst)
    cycle_counter += 1

print(input_lst)
