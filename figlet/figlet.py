import sys
from pyfiglet import Figlet

figlet = Figlet()
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in Figlet().getFonts():
        figlit=figlet.setFont(font=sys.argv[2])
        text = input("Input: ")
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    text = input("Input: ")
    print(figlet.renderText(text))
else:
    sys.exit("Invalid usage")
