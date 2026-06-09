# Список з 3 елементів з іншого списку випадкових чисел

import random

len_lst = random.randint(3, 10)
print(len_lst)

lst = []

for index_lst in range(len_lst):

    lst.append(random.randint(0, 100))

lst_1 = [lst[0], lst[2], lst[-2]]

print(lst)
print(lst_1)
