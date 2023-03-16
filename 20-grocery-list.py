alphabet = [chr(i) for i in range(65, 65+26)]

grocery_list = []

while True:
    try:
        item = input("").upper()
        grocery_list.append(item)
    except EOFError:
        break

list = list(dict.fromkeys(sorted(grocery_list)))

for item in list:
    print(f"{grocery_list.count(item)} {item}")
