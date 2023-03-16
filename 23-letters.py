import pyfiglet, sys

figlet = pyfiglet.Figlet()

if sys.argv[1] == "-f" or sys.argv[1] == "--font":
    figlet.setFont(font = sys.argv[2])

text = input("Input: ")

figlet.renderText(text)