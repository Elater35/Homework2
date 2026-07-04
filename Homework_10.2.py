# ДЗ 10.2. Знайти перше слово

def first_word(text):
    """ Пошук першого слова """

    first_word_ = ""

    for item in text:

        if item.isalpha():
            index_1 = text.index(item)

            # a) якщо перше слово є і останнім без знаків пунктуації чи пробілу в кінці тексту:
            if text[index_1:].isalpha():
                first_word_ = text[index_1:]
                return first_word_

            # для a) - варіант присвійного відмінку з "s" в кінці, наприклад, girls':
            elif text[index_1:-1].isalpha() and text[index_1:][-1] == "'":
                first_word_ = text[index_1:]
                return first_word_

            else:
                for item1 in text[index_1:]:
                    if not item1.isalpha() and item1 != "'":
                        index_2 = text[index_1:].index(item1)
                        first_word_ = text[index_1:index_1 + index_2]
                        return first_word_

    return first_word_


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'

assert first_word("") == "", 'Test7'
assert first_word(",,.  ;") == "", 'Test8'
assert first_word("C") == "C", 'Test9'
assert first_word("C++") == "C", 'Test10'
assert first_word("girls'") == "girls'", 'Test11'
assert first_word("   girls'.  ") == "girls'", 'Test12'
assert first_word(" /. hi") == "hi", 'Test5.1'
print('OK')
