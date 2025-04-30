def is_even(digit: int) -> bool:
    """ Перевірка чи є парним число
    param digit: Число для перевірки на парність
    type digit: int
    return: True якщо число парне, False якщо непарне
    return type: bool
    """
    return digit % 2 == 0

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')