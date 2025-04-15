import keyword
var_name = input( "Enter variable name: ")
my_lst = var_name.split("_")
result = "True"
if var_name[0] != "_" and not (var_name[0].isalpha() and var_name[0].islower()):
        result = "False1"
elif my_lst.count("") >= len(my_lst) > 2:
        result = "False2"
for a in my_lst:
    if a != "" and not (a.isalnum() and a.islower()):
        result = "False3"
    if keyword.iskeyword(a) and len(my_lst) < 2:
        result = "False4"
print(result)














