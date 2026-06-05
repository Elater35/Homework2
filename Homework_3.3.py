# Розділити один список на два списки.

input_lst = [2, 16, 3, "27, 5, 318", 7, 8, 429]

length_lst = len(input_lst)

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
