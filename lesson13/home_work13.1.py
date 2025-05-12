class Human:
    """ Клас для представлення людини """

    def __init__(self, gender, age, first_name, last_name):
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

    def __str__(self):
        """ Повертає рядкове представлення людини """
        return f"{self.first_name} {self.last_name} ({self.gender}, {self.age})"


class Student(Human):
    """ Клас для представлення студента, успадковується від Human """

    def __init__(self, gender, age, first_name, last_name, record_book):
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

    def __str__(self):
        """ Повертає рядкове представлення студента """
        return f"{self.first_name} {self.last_name} ({self.gender}, {self.age} age, {self.record_book})"


class Group:
    """ Клас для представлення групи студентів """

    def __init__(self, number):
        """
        Ініціалізація екземпляру класу Group.
        Аргументи:
            number (str): Номер групи
        """
        self.number = number
        self.group = set()

    def add_student(self, student):
        """
        Додає студента до групи.
        Аргументи:
            student (Student): Об'єкт студента для додавання
        """
        self.group.add(student)

    def delete_student(self, last_name):
        """
        Видалення студента за прізвищем.
        Аргументи:
            last_name (str): Прізвище студента
        """
        self.group = set(student for student in self.group if student.last_name != last_name)

    def find_student(self, last_name):
        """
        Пошук студента за прізвищем.
        Аргументи:
            last_name (str): Прізвище студента
        """
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        """ Повертає рядкове представлення всіх студентів группи """
        all_students = "\n".join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student("Female", 27, "Anna", "Smith","AN149")
print(st1)
print(st2)
print(st3)

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
print(gr.find_student('Anna'))
print(gr.find_student('Taylor'))
print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!