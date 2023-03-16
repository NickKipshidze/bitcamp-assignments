names = []

while True:
    try:
        names.append(input("Name: ").title())
    except EOFError:
        break
print("")

if len(names) > 2:
    print(f"Adieu, adieu, to {', '.join(names[:-1])} and {names[-1]}.")
elif len(names) == 2:
    print(f"Adieu, adieu, to {' and '.join(names)}.")
else:
    print(f"Adieu, adieu, to {names[0]}.")