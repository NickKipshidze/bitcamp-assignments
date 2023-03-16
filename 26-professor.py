import random

def main():
    level = get_level()
    score = 0

    for questions in range(10):
        numbers = [generate_integer(level), generate_integer(level)]

        print(numbers[0], "+", numbers[1], "=", end=" ")

        try:
            answer = int(input(""))

            if answer != sum(numbers):
                print("EEE")
            elif answer == sum(numbers):
                score += 1
        except:
            print("EEE")
        
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))

            if n > 0 and n < 4:
                break
        except:
            pass

    return n

def generate_integer(level):
    return int("".join([str(random.randint(0, 9)) for _ in range(level)]))

if __name__ == "__main__":
    main()