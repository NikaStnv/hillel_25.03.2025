agree = "так"
while agree == "так":
    numb_1 = int(input("Введіть перше число: "))
    numb_2 = int(input("Введіть друге  число: "))
    operation_1 = input("Введіть математичну дію над числами: ")
    if operation_1 == "+":
        print("Результат: ", numb_1 + numb_2)
    elif operation_1 == "-":(
        print("Результат: ", numb_1 - numb_2))
    elif operation_1 == "*":
        print("Результат: ", numb_1 * numb_2)
    elif operation_1 == "/":
        if numb_2 != 0:
            print("Результат: ", numb_1 / numb_2)
        else:
            print("Помилка - на 0 ділити не можна!")
    operation_2 = input("Бажаєте продавжити? ")
    if operation_2 != "так":
        agree = "ні"
print("Гарного дня!")
