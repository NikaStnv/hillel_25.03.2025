enter_users_numb = input ("Введіть 5-ти значне ціле число : ")
transform_int = int (enter_users_numb)
numb_1 = transform_int // 10000
numb_2 = (transform_int // 1000) % 10
numb_3 = (transform_int // 100) % 10
numb_4 = (transform_int // 10) % 10
numb_5 = transform_int % 10
print(numb_5 * 10000 + numb_4 * 1000 + numb_3 * 100 + numb_2 * 10 + numb_1)




