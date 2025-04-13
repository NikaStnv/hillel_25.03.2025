user_str = input("Enter text: ")
form_str1 = user_str.title()
form_str2 = "#"
for y in form_str1:
    if y.isalnum():
        form_str2 += y
    else:
        form_str2 += ""
    if len(form_str2) > 139:
        break
print(form_str2)
