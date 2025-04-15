user_str = input("Enter text: ")
lst_str = user_str.split(" ")
form_str = "#"
for b in lst_str:
    b = b[0].upper() + b[1:].lower()
    for c  in b:
        if c.isalnum():
            form_str += c
        if len(form_str) > 139:
            break
print(form_str)

