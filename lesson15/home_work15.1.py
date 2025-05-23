class Rectangle:
    """Клас, що представляє прямокутник з можливістю виконання математичних операцій"""

    def __init__(self, width: int | float, height: int | float):
        """Ініціалізує прямокутник з заданими шириною та висотою.
           Аргументи:
               width (int | float): ширина прямокутника (додатнє число)
               height (int | float): висота прямокутника (додатнє число)
               area (int | float): площа прямокутника (обчислюється автоматично)
        """
        self.width = width
        self.height = height
        self.area = width * height

    def get_square(self) -> int | float:
        """Повертає площу прямокутника.
           Повертає:
            int | float: площа прямокутника (width * height)
        """
        return self.area

    def __eq__(self, other: int | float) -> bool:
        """Перевизначення оператора == для порівняння площ прямокутників.
           Аргументи:
               other: інший об'єкт Rectangle для порівняння
           Повертає:
               bool: True якщо площі рівні, False - якщо ні
        """
        return self.area == other.area

    def __add__(self, other: "Rectangle") -> "Rectangle":
        """Перевизначення оператора + для додавання прямокутників.
           Новий прямокутник має:
               - середнє арифметичне всіх сторін як ширину
               - висоту, розраховану для збереження сумарної площі
           Аргументи:
                other: інший об'єкт Rectangle для додавання
           Повертає:
                Rectangle: новий об'єкт-результат додавання
        """
        new_width = (self.width + other.width + self.height + other.height) / 4
        return Rectangle(new_width, (self.area + other.area) / new_width)

    def __mul__(self, n: int | float) -> "Rectangle":
        """Перевизначення оператора * для масштабування прямокутника.
           Змінює розміри прямокутника, зберігаючи пропорції.
           Нова площа = стара площа * n.
           Аргументи:
               n (int | float): коефіцієнт масштабування (додатнє число)
           Повертає:
               Rectangle: новий масштабований прямокутник
        """
        return Rectangle(self.width * n ** 0.5, self.height * n ** 0.5)

    def __str__(self) -> str:
        """Перевизначення методу для зручного виведення інформації.
           Повертає:
               str: рядок з описом прямокутника
        """
        return f"Rectangle: width - {self.width}, height - {self.height}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'



