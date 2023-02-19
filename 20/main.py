#  # f = open("пон.txt", "w", encoding="utf-8") # создаст если нет , перезапишит если есть
#  # f.write("errrr\n")
#  # f.write("errrrr") f.close()
#
# name = input("Название файла: ")
# f = open(name + ".txt", "w", encoding="utf-8")
# msg = input("содержимое: ")
# while msg != "":
#     f.write(msg + "\n")
#     msg = input("содержимое: ")
#
# a = open("введите имя файла: ")
# f = open(a, 'r')
# content = f.readlines()
# print(content)
# v = len(content)
# for i in range(v):
#     print(f"{i+1})",content[i].strip())

f = open("zxc.txt", "r", encoding="utf-8")
text = f.readlines()
print(text)
count = 0
while text != []:
    x = text
    f = open("1.txt","w", encoding="utf-8")
    for i in elements:
        count += 1
        f = open(str(count) + .txt", "w", encoding="utf-8")
        for i in elements:
        f.write(i)
    f.close()
        del text[:3]