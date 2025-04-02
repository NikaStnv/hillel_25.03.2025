enter_users_number = input ("Введіть 4-oх значне число  використовуючи від 0 до 9 : ")
transformation_int = int (enter_users_number)
number_1 = transformation_int // 1000
number_2 = (transformation_int // 100) % 10
number_3 = (transformation_int // 10) % 10
number_4 = transformation_int % 10
print(number_1)
print(number_2)
print(number_3)
print(number_4)


