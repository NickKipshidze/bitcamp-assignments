import sys

def parse_arguments(arguments):
    if len(arguments) < 2:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    
    if arguments[1].split(".")[1] != "py":
        sys.exit("Not a Python file")

    try:
        file = open(arguments[1], "r")
    except:
        sys.exit("File does not exist")

    return file

def count_lines(file):
    lines = 0

    for line in file.readlines():
        line = line.strip()
        if len(line) > 1 and line[0] != "#":
            lines += 1

    return lines

def main(arguments):
    file = parse_arguments(arguments)
    
    print(count_lines(file))

if __name__ == "__main__":
    main(sys.argv)