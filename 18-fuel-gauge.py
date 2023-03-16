while True:
    fraction = input("Fraction: ").strip().split("/")

    try:
        percent = int(int(fraction[0])/int(fraction[1])*100)

        if percent > 100:
            pass
        elif percent >= 99:   
            print("F")
        elif percent <= 1:
            print("E")
        else:
            print(percent, "%", sep="")

    except ZeroDivisionError:
        print("Cant devide by zero;")
    except ValueError:
        print("Invalid fraction;")