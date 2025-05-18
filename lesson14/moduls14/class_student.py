from .class_human import Human


class Student(Human):
    """ Клас для представлення студента, успадковується від Human """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        """
        Ініціалізація екземпляру класу Student.
        Аргументи:
            gender (str): Стать студента
            age (int): Вік студента
            first_name (str): Ім'я студента
            last_name (str): Прізвище студента
            record_book (str): Номер залікової книжки
        """
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        """ Повертає рядкове представлення студента """
        return f"{self.first_name} {self.last_name} ({self.gender}, {self.age} age, {self.record_book})"

    def __eq__(self, object) -> bool:
        """
        Виконує порівняння студента за прізвищем abo заліковій книжці.
        Аргументи:
            object (Student або str): об'єкт для порівняння.
        Returns:
            bool: True якщо є рівність за вказаними аргументами, інакше False.
        """
        return self.last_name == object or self.record_book == object

    def __hash__(self) -> int:
        """
        Вираховує хеш-значення Студента на підставі його строкового представлення.
        Return:
            int: Хеш-значення
        """
        return hash(str(self))