# Types of coins
coins = [25, 10, 5]

# Expensive cola
amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    insert = int(input("Insert Coin: "))

    # Check if real coin
    if insert not in coins:
        # If not ask again
        continue

    # If its a real coin the decrease the amount_due
    amount_due -= insert

# amount_due will decrease and will be a negative number if change owed. So we get the absolute value of it.
print(f"Change Owed: {abs(amount_due)}")