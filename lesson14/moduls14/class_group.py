class Group:
    """ Клас для представлення групи студентів """

    def __init__(self, number: int) -> None:
        """
        Ініціалізація екземпляру класу Group.
        Аргументи:
            number (str): Номер групи
        """
        self.number = number
        self.group = set()

    def add_student(self, student: str) -> None:
        """
        Додає студента до групи.
        Аргументи:
            student (Student): Об'єкт студента для додавання
        Викликає:
        ValueError: Якщо кількість студентів вже дорівнює маскимальному значенню - 10
        """
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise ValueError("Досягнуто максимальної кількості студентів у групі")

    def delete_student(self, last_name: str) -> None:
        """
        Видалення студента за прізвищем.
        Аргументи:
            last_name (str): Прізвище студента
        """
        self.group = set(student for student in self.group if student.last_name != last_name)

    def find_student(self, last_name: str) -> str | None:
        """
        Пошук студента за прізвищем.
        Аргументи:
            last_name (str): Прізвище студента
        """
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        """ Повертає рядкове представлення всіх студентів группи """
        all_students = "\n".join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students}'