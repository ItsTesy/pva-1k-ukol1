import random

number = random.randint(1, 100)

while True:
    guess = int(input("hadej 1-100: "))
    if guess < number:
        print("vys")
    elif guess > number:
        print("min")
    else:
        print("spravne")
        break
