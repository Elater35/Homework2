# ДЗ 8.1. Додати 1 до числа.

def add_one(some_list):

    list_of_string_numbers = [str(item) for item in some_list]

    result_string = str(int("".join(list_of_string_numbers)) + 1)

    result_lst = [int(item) for item in result_string]

    return result_lst


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
