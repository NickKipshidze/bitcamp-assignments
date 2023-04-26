from datetime import datetime
import inflect

def calculate_days(birth, today):
    birth = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.strptime(today, "%Y-%m-%d")

    return int(str(today - birth).split(" ")[0])

def minutes_to_text(minutes):
    return inflect.engine().number_to_words(minutes) + " minutes"

def main():
    birth = input("Date of Birth: ")
    today = str(datetime.today()).split(" ")[0]

    days = calculate_days(birth, today)

    print(
        minutes_to_text(
            days*24*60
        )
    )

if __name__ == "__main__":
    main()