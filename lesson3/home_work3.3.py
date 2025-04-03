lst_main = [1, 2, 3, 4, 5]
qnt_lst_main = len(lst_main)
lst_1endindex = int(qnt_lst_main / 2) if qnt_lst_main % 2 == 0 else int(qnt_lst_main // 2 + 1)
lst_2startindex = int(qnt_lst_main / 2) if qnt_lst_main % 2 == 0 else int(qnt_lst_main // 2 + 1)
lst_1 = list(lst_main[:lst_1endindex])
lst_2 = list(lst_main[lst_2startindex:])
lst_3 = [lst_1, lst_2]
print(lst_main)
print(lst_1)
print(lst_2)
print(lst_3)
