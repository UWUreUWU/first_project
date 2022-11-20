import random

life = 10
length = 3

answer = random.randint(100, 999)
answer = str(answer)

while life:
    is_guessed = False
    print("=" * 10)

   # print("жизней:", life)
    print("жизней: ", end="")
    for _ in range(life):
        print("p-p, end=""")
    print()

    guess = input("предположение: ")
    if len(guess) != length or not guess.isdigit():
        print("число от 100 до 999, пожалуйста!")
        continue

    # проверка правельного ответа
    if guess == answer:
        print("пабеда")
        is_guessed = True
        break #выйти из while
    if is_guessed == False:

        for i in range(length):
            if guess[i] == answer[i]:
                print("Fermi")
                is_guessed = True
                break

    if is_guessed == False:
        for char  in  guess:
            if char in answer:
                print("Pico")
                is_guessed = True
                break

    if is_guessed == False:
        print("Bagels")

    life -= 1