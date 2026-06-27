# ДЗ 8.2. Паліндром.

def is_palindrome(text):

    text_to_palindrome = "".join([item.lower() for item in text if item.isalnum()])

    return text_to_palindrome == text_to_palindrome[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
