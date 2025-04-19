user_data = input("Enter numbers: ")
numbers = []
for x in user_data:
    numbers.append(int(x))
dct = { y : x for y, x  in enumerate(numbers,1)}
multiplication = 1
a = 1
while len(dct) >= 1:
    if numbers.count(0) > 0:
        multiplication *= 0
        break
    if a in dct:
        multiplication *= dct.pop(a)
        a += 1
    if len(dct) == 0 and multiplication > 9:
        (dct) = {y: int(x) for y, x in enumerate(str(multiplication), 1)}
        multiplication = 1
        a = 1
print(multiplication)
