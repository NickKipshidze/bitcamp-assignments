cost = float(
    input("How much was the meal? ")[1:]
)
percent = float(
    input("What precentage would you like to tip? ")[:-1]
)

tip = (50*15)/100

print(f"Leave ${tip:.2f}")