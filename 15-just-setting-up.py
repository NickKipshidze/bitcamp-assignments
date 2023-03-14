# Too simple
# Needs no comment

vowels = "aeiou"

word = input("")

for char in word:
    if char.lower() not in vowels:
        print(char, end="")
print("")