try: # попытаться
    number = int(input("ведите число: "))
    x = 5 / number
    print(x)
except ZeroDivisionError:  ловим исключения
    print("на ноль не дели")
except ValueError:
    print("хачу цифарку")
except Exception:
    print("одна ошибка и ты ошибся")
    name = input("введите имя: ")
    if name == "да"
        raise Exception("это имя под запретом")
except Exception as error_message:
    print("я запрещяю вам", error_message)
else:
    print(" ну вот такое можно")
finally:
    print("ы")

print("я отработав")
try:
    number = int(input("ведите число:"))
    x = 5 / number
except Exception:
    pass

if 3 == 3:
    pass # TODO:
