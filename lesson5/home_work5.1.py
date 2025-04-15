var_name = input( "Enter variable name: ")
key_str = """False,await,else,import,pass,None,break,except,in,raise,True,class,finally,is,return,and,
continue,for,lambda,try,as,def,from,nonlocal,while,assert,del,global,not,with,async,elif,if,or,yield"""
key_lst = key_str.split(",")
my_lst = var_name.split("_")
result = "True"
while True:
    if var_name[0] != "_" and not (var_name[0].isalpha() and var_name[0].islower()):
        result = result.replace("True", "False1")
        break
    if my_lst.count("") >= len(my_lst) > 2:
        result = result.replace("True", "False2")
        break
    for a in my_lst:
        if a != "" and not (a.isalnum() and a.islower()):
            result = result.replace("True", "False3")
            break
    for a in my_lst:
        for b in key_lst:
            if a.startswith(b) and len(my_lst) < 2:
                result = result.replace("True", "False4")
                break
    break
print(result)

















