def first_word(text: str) -> str:
    """ Пошук першого слова
    param text: Рядок в якому потрідно знайти перше слово
    type text: str
    return: Перше слово
    return type: str
    """
    word1 = ""
    i = 0
    while i < len(text):
        if text[i].isalpha() or text[i] == "'":
            word1 += text[i]
            i += 1
        else:
            if len(word1) != 0:
                break
            i += 1
    return word1


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')