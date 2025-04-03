lst = []
element_end = lst[-1] if len(lst) != 0 else ""
if len(lst) != 0:
    lst.pop(-1) and lst.insert(0, element_end)
    print(lst)
else:
    print(lst)