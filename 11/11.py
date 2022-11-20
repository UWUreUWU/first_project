# import random
# import datetime
#
# while True:
#     number = input("сколько дней рожнения мы генерим? (до 70)")
#     if not number.isdigit() or int(number) > 70 or int(number) < 2:
#         print("это по-твоему мешно? число от 2 до 70.")
#     else:
#         number = int(number)
#         break
#
# birthdays = []
# startOfYear = datetime.date(2022, 1, 1)
#
# for _ in range(number):
#     shiftOfDays =datetime.timedelta (random.randint(0,364))
#     birthday = startOfYear + shiftOfDays
#     birthdays.append(birthday)
#
# for index in range(number):
#     print(f"{index + 1}) {birthdays[index]}")
#
# print("=" * 10)
# for i in set(birthdays):
#     if birthdays.count(i) > 1:
#         print(f"- {i.strftime('%d.%m.%y')} встречатся {birthdays.count(i)} раза")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shoulb