import sys, csv

def parse_arguments(arguments):
    if len(arguments) < 3:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 3:
        sys.exit("Too many command-line arguments")

def check_filename(argument, check_exsistence = True):
    if argument.split(".")[1] != "csv":
        sys.exit("Not a CSV file")

    if check_exsistence:
        try:
            open(argument, "r")
        except:
            sys.exit(f"Could not read {argument}")
    
    return argument    

def main(arguments):
    parse_arguments(arguments)

    csvlist = []

    with open(check_filename(arguments[1]), newline="") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            if "," in row[0]:
                row = row[0].split(",") + row[1:]
                row[1] = row[1].strip()
            csvlist.append(row)
    
    afterfile = open(check_filename(arguments[2], False), "w")
    writer = csv.writer(afterfile)

    writer.writerows(csvlist)

if __name__ == "__main__":
    main(sys.argv)