# primer1 = lambda a, b: a + b + 1
#
# print(primer1(5, 10))
#
# answer = "Д"
# exit_triger = lambda yn: True if yn == "Д" else False
# print(exit_triger(answer))


# генератор списка (list comprehension)
# lst = []
# for i in range(1, 6):
#     lst.append(i)
# print(lst)
#
# lst = [i for i in range(1, 6)]
# # 1.всегда в []
# # 2. for in ...-> сколько элиментов в списке
# # 3. всё что перед for -> сам элемент списка
#
# c2f = lambda c: 9/5 * c + 32
# f2c = lambda f: (f-32)* 5/9
# c2k = lambda c: 273.15 + 5
# k2c = lambda k: - 273.15
# f2k = lambda f:c2k(f2c(f))
# degree = 203
# print(c2k(degree))
# from random import choice
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#          list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#          list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#          list("abcdefghijklmnopqrstuvwxyz"),
#          list("1234567890")
#         ]
# lst = []
# for i in range(6):
#     lst.append(choice(choice(chars)))
# code =  "".join(lst)
# ssilka = "сылка"
# d = {}
# # d = {"сылка" : "roflan"}
# if ssilka in d:
#     print("эта сылка есть в базе вт её код ->", d[ssilka])
# else:
#     d[ssilka] = code
#     print("сылка добавлена вот её код ->", d[ssilka])

a = 2
b = 5
yy1 = lambda a, b : b - a
print(yy1(a, b))

yy2 = lambda a, b : b + a

yy3 = lambda a, b : b / a

yy4 = lambda a, b : b * a

yy5 = lambda a, b : a / b

loloshka = lambda x : -x if x<0 else x
print(abs(-5))

logarifm = lambda a, b : math.log(b, a)
print(math.log(b, a))