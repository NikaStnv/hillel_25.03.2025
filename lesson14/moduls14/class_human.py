class Human:
    """ Клас для представлення людини """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        """
        Ініціалізація екземпляру класу Human.
        Аргументи:
            gender (str): Стать людини
            age (int): Вік людини
            first_name (str): Ім'я людини
            last_name (str): Прізвище людини
        """
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """ Повертає рядкове представлення людини """
        return f"{self.first_name} {self.last_name} ({self.gender}, {self.age})"
