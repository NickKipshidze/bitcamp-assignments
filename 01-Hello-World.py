# მეორე ვერსიისთვის
import random

def საწყისი_ვერსია() -> None:
    # სახელის ცვლადი
    name = input("What is your name? ")

    # გამარჯობას + სახელი = გამარჯობა ნიკა
    output = "Hello, " + name + ", nice to meet you!"

    # დავბეჭდოთ ჩვენი მისალმება
    print(output)

def ცვლადების_გარეშე() -> None:
    # ერთ ხაზზე, ცვლადების გარეშე.
    print("Hello,", input("What is your name? "), "nice to meet you!")

def მეორე_ვერსია() -> None:
    name = input("What is your name? ")

    # სავარაუდო მისალმებები
    # დაფორმატებული სტრინგები (f"")
    greetings = [
        f"Hello, {name}. Nice to meet you",
        f"Greetings, {name}.",
        f"Nice to see you {name}.",
        f"Hi {name}",
        f"Hello {name}. This code was written by Nick Kipshidze"
    ]

    # შემთხვევით ამოვარჩიოთ წევრი
    print(
        greetings[
            random.randint(0, len(greetings)-1)
        ]
    )

# შემდეგ ხაზზე გამოიძახე ფუნქცია!
# მაგალითი()
