from user import User

u1 = User("понов","пон","pon-pon","12345")
u2 = User()

users = [u1, u2]
l = input("введите логин: ")
p = input("введите пароль: ")
for chelovek in users:
    if chelovek.log_in(l, p):
        print("авторизация успешна")
        current = chelovek