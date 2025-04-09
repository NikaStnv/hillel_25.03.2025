lst_1 = [0, 1, 7, 2, 4, 8]
lst_2 = list(lst_1[::2])
x = sum(lst_2) * lst_1[-1] if len(lst_2) != 0 else 0
print(x)

# 2 variant
lst_1 = [1, 3, 5]
lst_2 = []
while lst_1[:] != []:
    lst_2.extend(lst_1[::2])
    x = sum(lst_2) * lst_1[-1]
    print(x)
    break
else:
    print(0)


