lst_1 = []
lst_2 = lst_1[::2]
result = 0
for x in lst_2:
    result += x * lst_1[-1]
print(result)




