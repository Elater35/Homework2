# Перемістити всі нулі до кінця списку.

input_lst = [2, 0, 0, 16, 0, 3, 27, 0, 5, 318, 7, 55, 9, 0]

number_zeros_of_lst = 0 # лічильник циклу

while number_zeros_of_lst < input_lst.count(0):
    input_lst.index(0)
if length_lst == 1:
    result_lst = [input_lst, []]
elif length_lst != 0 and length_lst % 2 == 0:
    result_lst = [input_lst[:length_lst // 2], input_lst[length_lst // 2:]]
elif length_lst % 2 == 1:
    result_lst = [input_lst[:length_lst // 2 + 1], input_lst[length_lst // 2 + 1:]]
else:
    result_lst = [[], []]

print(input_lst)
print(result_lst)
