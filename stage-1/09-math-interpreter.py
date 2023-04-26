# expression = input("Expression: ")
# print(float(eval(expression)))

expression = input("Expression: ").replace(" ", "")
math = []

num = " "
for char in expression:
    if char.isdigit():
        if num[-1].isdigit() == False:
            math.append(num)
            num = char
        else:
            num += char
    else:
        if num[-1].isdigit() == False:
            num += char
        else:
            math.append(num)
            num = char

math.append(num)

math = math[1:]

evaluation = float(math[0])

for i in range(2, len(math)):
    if math[i].isdigit():
        math[i] = float(math[i])
        if math[i-1] == "+":
            evaluation += math[i]
        if math[i-1] == "-":
            evaluation -= math[i]
        if math[i-1] == "*":
            evaluation *= math[i]
        if math[i-1] == "/":
            evaluation /= math[i]

print(evaluation)
