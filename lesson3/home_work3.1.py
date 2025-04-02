numb_1 = int(input("Введіть перше число: "))
numb_2 = int(input("Введіть друге  число: "))
operation = input("Введіть математичну дію над числами: ")
if operation == "+":
    print("Результат: ", numb_1 + numb_2)
elif operation == "-":
    print("Результат: ", numb_1 - numb_2)
elif operation == "*":
    print("Результат: ", numb_1 * numb_2)
elif operation == "/" and numb_2 != 0:
    print("Результат: ", numb_1 / numb_2)
else: print("Помилка - на 0 ділити не можна!")





