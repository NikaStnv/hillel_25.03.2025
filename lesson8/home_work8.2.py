def is_palindrome(text: str) -> bool:
    text = text.lower()
    text_alnum = ""
    for x in text:
        if x.isalnum():
            text_alnum += x
    return True if text_alnum == text_alnum[::-1] else False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
