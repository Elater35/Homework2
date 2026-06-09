# Сума чисел з парними індексами списку цілих чисел, помножена на останнє число списку.

# input_lst = []
# input_lst = [0]
# input_lst = [0, 2, 16, 0, 3, 27, 0, 5, 318, 7, 55, 9, 0]

input_lst = [2, 16, 3, 27, 5, 318, 7, 55, 6]
print(input_lst)

result = None # Сума чисел з парними індексами списку цілих чисел, помножена на останнє число списку
length_lst = len(input_lst)

if length_lst == 0 or input_lst[-1] == 0:
    result = 0
    print("Сума чисел з парними індексами списку цілих чисел, помножена на останнє число списку =", result)

else:
    index_lst = 0
    sum_of_numbers_of_even_indexes = 0

    while index_lst < length_lst:
        if index_lst % 2 != 0:
            index_lst += 1
            continue
        sum_of_numbers_of_even_indexes += input_lst[index_lst]
        index_lst += 1

    result = sum_of_numbers_of_even_indexes * input_lst[-1]
    print("Сума чисел з парними індексами списку цілих чисел, помножена на останнє число списку =", result)
