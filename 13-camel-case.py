# Get user input
camel_case = input("camelCase: ")
snake_case = ""

# "Read" the camel_case string
for char in camel_case:
    # If the char is upper case
    if char == char.upper():
        snake_case += "_"

    snake_case += char.lower()

# Output snake_case
print(f"snake_case: {snake_case}")