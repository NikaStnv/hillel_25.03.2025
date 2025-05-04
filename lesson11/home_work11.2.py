def generate_cube_numbers(end: int):
    """ Генератор кубів чисел від 2 до вказаної величини (включно)
    param end: Максимально можлива величина числа у кубі
    type end: int
    """
    for element in range(2, round(end ** (1 / 3)) + 1):
        if element ** 3 <= end:
            yield element ** 3



from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
