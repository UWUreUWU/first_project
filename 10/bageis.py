import random

life = 10
length = 3

answer = random.randint(100, 999)
answer = str(answer)

while life:
    is_guessed = False
    print("=" * 10)

    print("жизней:", life)

    guess = input("предположение: ")
    if len(guess) != length or guess.isdigit():
        print("число от 100 до 999, пожалуйста!")
        continue