enter_users_numb = input ("Введіть 5-ти значне ціле число : ")
transform_int = int (enter_users_numb)
numb_1 = int(transform_int // 10000.01)
numb_2 = int((transform_int % 10000.01) * 0.001)
end3_numb = int(transform_int - (numb_1 * 10000 + numb_2 * 1000))
numb_3 = int(end3_numb // 100.01)
numb_4 = int((end3_numb % 100.01) * 0.1)
numb_5 = int(transform_int - (numb_1 * 10000  + numb_2 * 1000 + numb_3 * 100 + numb_4 * 10))
print(numb_5 , numb_4 , numb_3 , numb_2 , numb_1)



