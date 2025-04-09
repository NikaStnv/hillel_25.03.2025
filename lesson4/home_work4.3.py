import random
rnd_lst = [random.randint(1,10) for qnt in range(random.randint(3, 10))]
my_lst = [rnd_lst[0], rnd_lst[2], rnd_lst[-2]]
print(rnd_lst)
print(my_lst)

