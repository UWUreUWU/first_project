# def hello(x): # объявили функцию + ждём аргументы x
#     return "hello" + x
#
# print(hello("эммм"))
#
# l = lambda x, b: "hello" + b + x
# print(l("Лютый", "Черкаш"))
#
# l = [for i in range(1, 6)]
# print(l)

import time
import random
print("Время проверить твою ловкость и скорость и понять, кто самый быстрый стрелок на западе! Когда увидишь 'СТРЕЛЯЙ', у тебя будет 0.3 секунды чтобы нажать Enter. Но если ты нажмёшь Enter раньше, то ты проиграл.")

input("надми Enter чтобы начать")
print("время пострелять")
time.sleep(random.randint(1, 5))


start = time.time()
input("BOOM")
end = time.time()
delta = end - start
print(f"{delta}cek")
if delta > 0.01:
    print("фальшстарт")

elif delta > 0.3:
    print("АХАХАХА, ну ты и чmо безрукое ")
else:
    print("о, круто")