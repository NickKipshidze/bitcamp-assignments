alphabet = [chr(i) for i in range(65, 65+26)]

grocery_list = []

while True:
    item = input("").upper()

    # I didnt understand control-d thing
    # Doesnt work on my machine
    if item == "DONE":
        break

    grocery_list.append(item)

list = list(dict.fromkeys(sorted(grocery_list)))

for item in list:
    print(f"{grocery_list.count(item)} {item}")