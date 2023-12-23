import sys

def main():
    lines = 0
    stripedLines = []
    sysMinMax(2)
    extension(".py")

    try:
        with open(sys.argv[1], "r") as file:
            saveLines = file.readlines()
            for line in saveLines:
                stripedLines.append(line.lstrip())
            for line in stripedLines:
                if not line.startswith("#") and len(line) != 0:
                    lines += 1
        print(lines)

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


def extension(n):
    if not sys.argv[1].endswith(n):
        n = n.upper().replace(".", "")
        sys.exit(f"Not a {n} file")


if __name__ == "__main__":
    main()