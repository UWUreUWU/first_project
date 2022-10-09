# # # # # # alphabet = "АБВГДЕЖЗИ"
# # # # # #
# # # # # # print(alphabet[::-1])
# # # # # # # [start:end:step]
# # # # #
# # # # # phrase = "антон"
# # # # # print(phrase.upper())
# # # # # print(phrase.lower())
# # # # #
# # # # # phrase1 = "я фраза, эээ..."
# # # # # print(phrase1.ca)
# # # # familiya = input("фамилия: ")
# # # # imya = input("Имя: ")
# # # # otchestvo = ("Отчество: ")
# # # # print(familiya, imya[0] + ".", otchestvo[0] + ".")
# # # # print(f"{familiya} {imya[0]}. {otchestvo[0]}.")
# # # #
# # # # x = input()
# # # # print(x.count('a'))
# # # # print(x.lower().count('a'))
# # # x = input("Введите фразу, разделяя слоа запятыми: ")
# # # lst = x.split(",")
# # # lst.pop(0)
# # # print(lst)
# # phrase = input("Введите фразу: ")
# # find = input("то меняем:")
# # replace = input("На что меняем: ")
# #
# # print(phrase)
# phrase = input("Введите фразу: ")
# print(phrase.replace("йо", "ё"))
# alphabet = {
#     "a": "a",
#     "б": "b",
#     "в": "v",
#     "г": "g",
#     "д": "d",
# }
# x = input("Введите фразу чего-то: ")
# rus = ""
# for bukva in x:
#     rus = rus + alphabet[bukva]
# print(rus)
email = input("Введите почту: ")
print(email.split(@))
login = email.split("@")[-1]
print("Логин: ")
print("Домэн: ")