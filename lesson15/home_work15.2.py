class Fraction:
    """ Клас для роботи з дробами. Виконує функції додавання, множення, віднімання та порівняння"""

    def __init__(self, a: int, b: int) -> None:
        """
        Ініціалізація дробі з чиселником "a" та знаменником "b".
        Аргументи:
            a (int): чисельник дробі
            b (int): знаменник дробі (не може дорівнювати 0)
        # Викликає:
        # ValueError: Якщо знаменник (b) встановлено 0
        #             # або дріб неправильний (модуль а більше модуля b)
        """
        # if b == 0:
        #     raise ValueError("Знаменник не може дорівнювати 0")
        # if abs(a) >= abs(b):
        #     raise ValueError(f"Неправильний дріб {a}/{b}")
        self.a = a
        self.b = b

    # def __setattr__(self, name: str, value: int) -> None:
    #     """
    #     Встановлює атрибути з перевіркою на нульовий знаменник.
    #     Аргументи:
    #         name (str):  Ім'я атрибуту ("а " або "b")
    #         value (int): Значення атрибуту
    #     Викликає:
    #     ValueError: Якщо знаменник (b) встановлено 0
    #     """
    #     super().__setattr__(name, value)
    #     if hasattr(self, "a") and hasattr(self, "b"):
    #         if name == "b"  and value == 0:
    #             raise ValueError("Знаменник не може дорівнювати 0")
    #         if abs(self.a) > abs(self.b):
    #             raise ValueError(f"Неправильний дріб {self.a}/{self.b}")

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """
        Множення двох дробів
        Аргументи:
            other: Інша дріб для множення
        Повертає:
            Нова дріб як результат множення
        """
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """
        Додавання двох дробів
        Аргументи:
            other: Інша дріб для додавання
        Повертає:
            Нова дріб як результат додавання
        """
        return Fraction(self.a * other.b + self.b * other.a , self.b * other.b)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """
        Віднімання двох дробів
        Аргументи:
            other: Інша дріб для віднімання
        Повертає:
            Нова дріб як результат віднімання
        """
        return Fraction(self.a * other.b - self.b * other.a , self.b * other.b)

    def __eq__(self, other: 'Fraction') -> 'Fraction':
        """
        Порівняння двох дробів
        Аргументи:
            other: Інша дріб для порівняння
        Повертає:
            True, якщо перша дріб дорівнює другій, інакше False
        """
        return self.a * other.b == other.a * self.b

    def __gt__(self, other: 'Fraction') -> 'Fraction':
        """
        Порівняння двох дробів
        Аргументи:
            other: Інша дріб для порівняння
        Повертає:
            True, якщо перша дріб більше, інакше False
        """
        return self.a * other.b > other.a * self.b

    def __lt__(self,other: 'Fraction') -> 'Fraction':
        """
        Порівняння двох дробів
        Аргументи:
            other: Інша дріб для порівняння
        Повертає:
            True, якщо перша дріб менше, інакше False
        """
        return self.a * other.b < other.a * self.b

    def __str__(self) -> str:
        """
        Строкове представлення дробі.
        Повертає:
            Строка у форматі 'Fraction(a, b)'
        """
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
