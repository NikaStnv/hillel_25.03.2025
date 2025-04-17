import string
user_data = input("Введіть літери через дефіс: ").split("-")
str = string.ascii_letters
lst = "-".join(str).split("-")
dct = {key : value for value, key in enumerate(str, 0)}
if dct[user_data[0]]  < dct[user_data[1]]:
    result = "".join(lst[dct[user_data[0]]:dct[user_data[1]]]) + user_data[1]
else:
    # result = "".join(lst[dct[user_data[-1]]:dct[user_data[0]]]) + user_data[0]
    result = "".join(lst[dct[user_data[0]]:dct[user_data[1]]:-1]) + user_data[1]
print(result)
