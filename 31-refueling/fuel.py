def main():
    fraction = input("Fraction: ")
    print(
        gauge(
            convert(fraction)
        )
    )

def convert(fraction):
    # Mistake here
    # fraction = fraction.strip().split("/")
    return int(int(fraction[0])/int(fraction[1])*100)

def gauge(percentage):
    if percentage >= 99:   
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()