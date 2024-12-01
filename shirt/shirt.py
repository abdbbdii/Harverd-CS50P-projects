import sys
from os import path
from PIL import Image, ImageOps


def main():
    sysMinMax(3)
    File1, Extension1 = path.splitext(sys.argv[1])
    File2, Extension2 = path.splitext(sys.argv[2])

    if Extension1 != ".jpg" and Extension1 != ".jpeg" and Extension1 != ".png":
        sys.exit("Invalid input")
    elif Extension2 != ".jpg" and Extension2 != ".jpeg" and Extension2 != ".png":
        sys.exit("Invalid output")
    elif Extension1.casefold() != Extension2.casefold():
        sys.exit("Input and output have different extensions")
    else:
        pass

    try:
        with Image.open("shirt.png") as shirt:
            inpt = Image.open(sys.argv[1])
            size = shirt.size
            inpt = ImageOps.fit(inpt, size=size)
            inpt.paste(shirt, shirt)
            inpt.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("File does not exist")


def sysMinMax(n):
    try:
        if len(sys.argv) != n:
            raise IndexError
    except IndexError:
        if len(sys.argv) < n:
            return sys.exit("Too few command-line argument")
        elif len(sys.argv) > n:
            return sys.exit("Too many command-line argument")


if __name__ == "__main__":
    main()
