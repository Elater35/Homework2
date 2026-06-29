# ДЗ 9.1. Визначити популярність певних слів у тексті

def popular_words(text, words):

    list_text = text.lower().split()

    popular_words_dict = {key: list_text.count(key) for key in words}

    return popular_words_dict


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
