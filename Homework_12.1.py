# ДЗ 12.1. Генератор простих чисел

def prime_generator(end):

    lst_prime_numbers = list(range(3, end + 1, 2))
    lst_prime_numbers.insert(0, 2)

    for item in lst_prime_numbers:

        if item in (2, 3):
             yield item

        else:
            less_sqrt = 2
            while less_sqrt <= int(item ** 0.5):
                if item % less_sqrt  == 0:
                    break
                else:
                    less_sqrt += 1
                    if less_sqrt > int(item ** 0.5):
                        yield item



from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
