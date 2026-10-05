import random

while True:
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("hadej 1-100: "))
        except ValueError:
            print("to neni cislo")
            continue

        if guess < 1 or guess > 100:
            print("musi to byt od 1 do 100")
            continue

        attempts += 1

        if guess < number:
            print("vys")
        elif guess > number:
            print("min")
        else:
            print("gratuluju, uhodl jsi to na", attempts, "pokusu")
            break

    again = input("hrat znovu? (a/n): ")
    if again != "a":
        break
