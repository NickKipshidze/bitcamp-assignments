def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check for length
    if not 6 >= len(s) >= 2:
        return False
    
    # Check if first two symbols are numbers
    if s[0].isdigit() or s[1].isdigit():
        return False
    
    number_encountered = False
    for char in s:
        # If first number is zero then invalid
        if char == "0" and number_encountered == False:
            return False
        
        if char.isdigit():
            number_encountered = True
        # If number in middle of the plate, Then invalid
        elif number_encountered:
            return False
    
    # If the function got to this point, then valid.
    return True

main()
