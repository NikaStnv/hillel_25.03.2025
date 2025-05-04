def prime_generator(end: int):
    """ Генератор простих чисел
    param end: Останне число діапазану простих чисел
    type end: int
    """
    for element in range(2, end + 1):
        if not any(element % x == 0 for x in range(2, element)):
            yield element


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
