class Counter:
    """
    Простий лічильник із настроюваним діапазоном і кроковими операціями.
        Атрибути:
        current (int): поточне значення лічильника
        min_value (int): Мінімально дозволене значення
        max_value (int): Максимально дозволене значення
    """

    def __init__(self, current: int = 1, min_value: int = 0, max_value: int = 10) -> None:
        """ Ініціалізація лічильника.
            Аргументи:
            current (int): Початкове значення (за замовчуванням: 1)
            min_value (int): Мінімальне значення (за замовчуванням: 0)
            max_value (int): максимальне значення (за замовчуванням: 10)
            Викликає:
            ValueError: якщо current виходить за межі min_value або max_value
        """
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start: int) -> None:
        """ Встановлення початкового значення лічильника.
            Аргументи:
            current (int): Початкове значення
        """
        self.current = start

    def set_max(self, max_max: int) -> None:
        """ Встановлення максимального значення лічильника.
            Аргументи:
            max_max (int): максимальне значення
        """
        self.max_value = max_max

    def set_min(self, min_min: int) -> None:
        """ Встановлення мінімального значення лічильника.
            Аргументи:
            min_min (int): мінімальне значення
        """
        self.min_value = min_min

    def step_up(self) -> None:
        """
        Збільшує поточний показник лічильника на 1
        Викликає:
        ValueError: Якщо поточне значення лічильника вже дорівнює маскимальному значенню
        """
        if self.current < self.max_value:
           self.current += 1
        else:
           raise ValueError("Достигнут максимум")

    def step_down(self) -> None:
       """
       Зменшує поточний показник лічильника на 1
       Викликає:
       ValueError: Якщо поточне значення лічильника вже дорівнює мінімальному значенню
       """
       if self.current > self.min_value:
           self.current -= 1
       else:
           raise ValueError("Достигнут минимум")

    def get_current(self) -> int:
       """ Повертає поточне значення лічильника """
       return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'