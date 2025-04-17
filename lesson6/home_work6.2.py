user_data = int(input("Введіть кількість секунд у діапазоні від 0 до 8640000: "))
t = 60
days = user_data // (24 * (t ** 2))
hours = str((user_data % (24 * (t ** 2)) // (t ** 2))).zfill(2)
minutes = str((user_data % (t ** 2)) // t).zfill(2)
seconds = str(user_data % t).zfill(2)
dct = {'дні' : days,
       'години' : hours,
       'хвилини' : minutes,
       'секунди' : seconds}
if (str(days).endswith("11") or str(days).endswith("12") or str(days).endswith("13")
        or str(days).endswith("14") or str(days).endswith("0")):
       dct['відмінювання'] = "днів"
elif str(days).endswith("2") or str(days).endswith("3") or str(days).endswith("4"):
       dct['відмінювання'] = "дні"
elif (str(days).endswith("5") or str(days).endswith("6") or str(days).endswith("7")
      or str(days).endswith("8") or str(days).endswith("9")):
       dct['відмінювання'] = "днів"
else:
       dct['відмінювання'] = "день"
print(f"{dct['дні']} {dct['відмінювання']}, {dct['години']}:{dct['хвилини']}:{dct['секунди']}")






