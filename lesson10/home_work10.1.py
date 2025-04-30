def pow(x: int) -> int:
    return x ** 2
def some_gen(begin, end, func):
    """
    begin: перший елемент послідовності
    end: кількість елементів у послідовності
    func: функція, яка формує значення для послідовності
    """
    lst = [begin]
    count = 0
    while len(lst) <= end:
        lst.append(func(lst[-1]))
        yield lst[count]
        count += 1


from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')