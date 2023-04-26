import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # You’re welcome, but not required, to use re and/or sys.

    words = s.lower().split(" ")
    words = [word.strip("!@#$%^&*()<>,.?") for word in words]

    return words.count("um")

if __name__ == "__main__":
    main()