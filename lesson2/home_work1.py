enter_users_number = input ("Введіть 4-oх значне число  використовуючи від 0 до 9 : ")
transformation_int = int (enter_users_number)
number_1 = int(transformation_int // 1000.01)
number_2 = int((transformation_int % 1000.01) * 0.01)
end2_number = int(transformation_int - (number_1 * 1000 + number_2 * 100))
number_3 = int(end2_number // 10)
number_4 = int(end2_number % 10)
print(int(number_1))
print(int(number_2))
print(int(number_3))
print(int(number_4))

