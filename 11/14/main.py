# 1) повторения исключения
# d1 = {"ггг", "ггг", "e"}
# # 2) неупорядоченные
# print(d1)
# 3) пустое множество - только set()
# 4) внутри толко неизменяемые данные

# словари
# 1) изменяемый тип данных
# x = ("ooo")
# d = {
#     ggg: 1,
# }
# print(d)
# 3) пустой словарь = dict () или {}

# phrase = "маша ты где? мАШа загОРает.lower()"
# print(phrase)
# spisok_nechist = list("!,.?")
# phrase_cleared = ""
# d = {}
# for tadjikistan  in phrase:
#     if tadjikistan not in spisok_nechist:
#      phrase_cleared += tadjikistan
# l = phrase_cleared.split(" ")
# print(l)
# for bogdan in l:
#     if bogdan not in d:
#         d[bogdan] = 1
#     else:
#         d[bogdan] += 1
# print(d)
# 2 задача
# s = 0
# d = {"хлеб": 1000,
#      "молоко": 1.5,
#      "сырок Б.Ю. алекс.": 47,
#      "елка": 50,
#      }
# for price in d.values():
#     s + price
# print(s)
# phrase = "маша ты где? мАШа загОРает.lower()"
# print(phrase)
# spisok_nechist = list("!,.?")
# phrase_cleared = ""
# d = {}
# for tadjikistan  in phrase:
#     if tadjikistan not in spisok_nechist:
#      phrase_cleared += tadjikistan
# l = phrase_cleared.split(" ")
# print(l)
# for bogdan in l:
#     if bogdan not in d:
#         d[bogdan] = 1
#     else:
#         d[bogdan] += 1
# print(d)
#
# maxi = max(d.values())
# for (k, values) in d.items():
#         print(f"ключь:{key}, значение:{values}")
#     print(values)

# 4 задача
d = {
    1:2,
    4:2,
    6:2,
    8:2,
    "ttt":2,
}
# one = 1
# two = 2
# print(one, two)
# one, two = two, one
# print(one, two)


d["ttt"], d[4] = d[4], d["ttt"]

del d[6]

d["new_key"] = "new_values"
print(d)