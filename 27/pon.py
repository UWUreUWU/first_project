# c1 = input("Введите первый цвет:").strip().lower()
# c2 = input("Введите второй цвет:").strip().lower()
# c = ("крастный, желтый, синий")
#
# if c1 not in c or c2 not in c:
#     print("Один из основных цветов введён неверно!")
# elif (c1 == c[0] and c2 == c[1] or c1 == c[1] and c2 == c[0]):
#     print("ораньжевый")
# elif (c1 == c[0] and c2 == c[1] or c1 == c[1] and c2 == c[2]):
#     print("зеленый")
# elif (c1 == c[0] and c2 == c[2] or c1 == c[2] and c2 == c[0]):
#     print("фиолетовый")
# else:
#     print(c1.capitalize())
#
# first_lesson = input("ведите время начала уроков ")
# len_lesson = int(input("введите длительность уроков"))
# break_time = int(input("введите длительность перемены"))
# lesson_count = int(input("введите кол-во уроков"))
# hours, minutes = first_lesson.split(":")
# hours, minutes = int(hours), int(minutes)
# time = hours*60 + minutes
# for i in range(lesson_count+1):
#     print(f"{i+1} урок:", end="")
#     print(f"{str(hours).rjust(2,'0')}:{str(minutes).rjust(2, '0')} - ", end="")
#     time += len_lesson
#     hours = time // 60
#     minutes = time % 60
#     print(f"{str(hours).rjust(2,'0')}:{str(minutes).rjust(2, '0')}")
#     time += 10
#     hours = time // 60
#     minutes = time % 60

col_zomb = int(input("кол-во зомби в начале эпидемии:"))
vozm_zaraz = int(input("кол-во возможно заражоных людей:"))
day = int(input("на какой делается подсчот:"))
print((f"1 день:{col_zomb}"))
for i in range(2, day+1):
    col_zomb = col_zomb * vozm_zaraz + col_zomb
    print(f"{i}день:{col_zomb*vozm_zaraz+col_zomb}")