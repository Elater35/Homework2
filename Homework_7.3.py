# ДЗ 7.3. Пошук підрядка.

def second_index(text, some_str):

    index_first_ = text.find(some_str)
    index_second_ = None
    some_str_len = len(some_str)

    if index_first_ == -1:
        return index_second_

    elif text[index_first_ + some_str_len:].find(some_str) == -1:
        return index_second_

    else:
        index_second_ = text[index_first_ + some_str_len:].find(some_str) + index_first_ + some_str_len
        return index_second_


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
