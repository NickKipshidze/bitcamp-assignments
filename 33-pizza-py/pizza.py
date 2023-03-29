import sys, csv, tabulate

def parse_arguments(arguments):
    if len(arguments) < 2:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    
    if arguments[1].split(".")[1] != "csv":
        sys.exit("Not a CSV file")

    try:
        open(arguments[1], "r")
    except:
        sys.exit("File does not exist")

    return arguments[1]

def main(arguments):
    csvlist = []

    with open(parse_arguments(arguments), newline="") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            csvlist.append(row)

    table = csvlist[1:]
    headers = csvlist[0]

    print(tabulate.tabulate(table, headers, tablefmt="grid"))

if __name__ == "__main__":
    main(sys.argv)