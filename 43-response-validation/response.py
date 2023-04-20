import validators

def main() -> None:
    text = input("What's your email address? ")

    if validate(text):
        print("Valid")
    else:
        print("Invalid")

def validate(text) -> bool:
    return bool(validators.email(text))

if __name__ == "__main__":
    main()