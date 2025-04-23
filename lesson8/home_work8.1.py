def add_one(some_list: list) -> list:
    int_from_lst = int("".join([str(x) for x in some_list]))
    add_1 = str(int_from_lst + 1)
    lst_from_add_1 = list(int(y) for y in add_1)
    return lst_from_add_1


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")


