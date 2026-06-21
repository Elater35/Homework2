# ДЗ 6.3. Добуток чисел.

input_number = input("Enter any integer: ")

result_ = int(input_number)

if "0" in input_number:
    result_ = 0
else:
    while result_ > 9:
        iterate_str = str(result_)
        result_ = 1
        for item in iterate_str:
            result_ *= int(item)

print(input_number, " -> ", result_)
