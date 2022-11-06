# import random
# import time
#
# print("время пострелять.")
#
# is_game = "y"
# while is_game == "y":
# time.sleep(0.5)
# print("*зарежаем револьвер*")
# time.sleep(2.5)
# print("*раскручиваем барабан*")
# time.sleep(1.5)
# print(3)
# time.sleep(1)
# print(2)
# time.sleep(1)
# print(1)
# time.sleep(1)
# print("выстрел")
#
# slots =[1, 2, 3, 4, 5, 6]
# patron = random.choice(slots)
# our = random.choice(slots)
#
# if patron == our:
#     print("есть пробитие")
#     is_game = "n"
# else:
#     print("повезло")
#     x = input("играем дальше? y - да, n - нет")
#     if x == "n":
#         is_game = "n"
#
#
# lst = ["Антон1" , "Антон2" , "Антон3" , "Антон4" ]
# for antoha in lst:
#     print(antoha, end="a")
#
# print()
# for i in range(0, 10):
#     print("пон")
#
# word = input("введите слово: ")
# while word:
#     print(word)
#     word = word[:-1]
#
# x = int(input("введите цифру: "))
# while x: # усли =0 то работает
#     x-= 1
#     if x % 2 == 0:
#         print(x, end=" ")

x = int(input("введите циру: "))
while x != 1:
    step += 1:
    if x % 2 == 0:
        print(f"{step})", end=" ")
        print(x, "* 3 + 1 =", end = " ")
        x = x // 2
        print(x)

    else:
        x = 3 * x + 1
        print(x)
print("шагов:",step)