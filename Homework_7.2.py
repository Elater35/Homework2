# ДЗ 7.2. Модифікувати рядок.

def correct_sentence(text):

    if text.strip()[-1] in (".", "!", "?"):
        text_result = text.strip()
    else:
        text_result = text.strip() + "."

    if not text_result[0].istitle():
        text_result = text_result[0].title()+text_result[1:]

    return text_result


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')