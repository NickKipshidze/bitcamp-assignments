def main():
    text = input("I am expecting a str: ")
    print(shorten(text))

def shorten(word):
    # Good code here
    # return "".join([char for char in word if char.lower() not in "aeiou"])

    # Oh no a mistake ):
    return "".join([char for char in word if char not in "aeiou"]) 
    # I better test it if it works


if __name__ == "__main__":
    main()