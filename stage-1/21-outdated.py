months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    # MM/DD/YYYY
    date = input("Date: ")

    # YYYY/MM/DD
    if len(date.split("/")) > 2:
        mm, dd, yyyy = date.split("/")
    else:
        date = date.replace(",", "").split(" ")

        for i in range(len(date)):
            if date[i].title() in months:
                mm = months.index(date[i].title())+1
            
            if date[i].isdigit():
                if int(date[i]) < 32:
                    dd = date[i]
                else:
                    yyyy = date[i]
    
    if int(mm) <= 12 and int(dd) <= 31:
        print(f"{yyyy}-{mm:0>2}-{dd:0>2}")