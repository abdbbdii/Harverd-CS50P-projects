import sys


def main():
    # Examples:
    sysMinMax(2)
    extension(".txt")


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