import random

while True:
    try:
        n = int(input("Level: "))

        if n > 0:
            break
    except:
        pass

number = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))

        if guess == number:
            print("Just right!")
        elif guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
    except:
        pass