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


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 30, 'Tom', 'Cat', 'AN143')
st4 = Student('Female', 25, 'Jerry', 'Mouse', 'AN146')
st5 = Student("Female", 27, "Anna", "Smith","AN149")
st6 = Student("Female", 18, "Sarah", "Adams", "AN159")
st7 = Student("Male", 21, 'Piter', 'Pen', 'AN160')
st8 = Student("Female", 24, "Bella", "Rosie","AN161")
st9 = Student("Male", 19, "John", "Abrams", "AN121")
st10 = Student("Male", 22, "Mike", "Tison", "AN128")
st11 = Student("Female", 22, "Olivia", "Anderson", "AN129")

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
gr.add_student(st11)

print(gr)

