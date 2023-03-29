import sys
from PIL import Image

def parse_arguments(arguments):
    if len(arguments) > 4:
        sys.exit("Too many command-line arguments")
    if len(arguments) < 4:
        sys.exit("Too few command-line arguemnts")
    
    if arguments[1].split(".")[-1] not in ["jpg", "jpeg", "png"]:
        sys.exit("Invalid input")
    if arguments[2].split(".")[-1] not in ["jpg", "jpeg", "png"]:
        sys.exit("Invalid input")
    try:
        open(arguments[1], "r")
        open(arguments[2], "r")
        file_shirt = arguments[1]
        file_character = arguments[2]
    except:
        sys.exit("Invalid input")
    
    file_output = arguments[3]

    return file_shirt, file_character, file_output

def main(arguments):
    file_shirt, file_character, file_output = parse_arguments(arguments)

    img_character = Image.open(file_character)
    img_shirt = Image.open(file_shirt).resize(img_character.size)

    img_character.paste(img_shirt, (0, 0), img_shirt)
    img_character.save(file_output)

if __name__ == "__main__":
    main(sys.argv)