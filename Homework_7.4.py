# ДЗ 7.4. Пошук спільних елементів

def common_elements():

	lst_1 = []
	lst_2 = []

	for item in range(100):

		if item % 3 == 0:
			lst_1.append(item)

		if item % 5 == 0:
			lst_2.append(item)

	set_result = set(lst_1).intersection(set(lst_2))

	return set_result


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
