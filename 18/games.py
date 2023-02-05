import easygui
import random

def rock_paper_scissors():
    b="img/бумага.png"
    k="img/камень.png"
    n="img/рожнецы.png"
    user=easygui.buttonbox(
    images=[b, k, n],
        choices=("выйти",),
    )
    #comp=random.choice([b,k,n])
    comp = b
    if user == b and comp == b:
        easygui.msgbox(msg="ничья")
    elif user == b and comp == k:easygui.msgbox(msg="ты выйграл")
    elif user == b and comp == n:easygui.msgbox(msg="лол")
    elif user == k and comp == n:easygui.msgbox(msg="эээ")
    elif user == n and comp == n:easygui.msgbox(msg="пон")
    else:easygui




def guess_the_number():
    chislo = random.randint(1, 100)
    gn = easygui.integerbox(upperbound=100, lowerbound=1, msg=f"отгодай число от 1 до 100!")
    while gn != chislo:  # пока не угадали
        if gn > chislo:
            gn=easygui.integerbox(upperbound=100, lowerbound=1, msg=f"нееееееет{gn}", image="img/м.png")
        elif gn < chislo:
            gn=easygui.integerbox(upperbound=100, lowerbound=1, msg=f"нееееееет{gn}", image="img/б.png")
    gn = easygui.msgbox(msg="ура",image="img/uwu.png")  # отработает после отгадывания

games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()

