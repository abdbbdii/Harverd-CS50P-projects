import csv
import sys
from tabulate import tabulate

def main():
    table = []
    sysMinMax(2)
    extension(".csv")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
        print(table)
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
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
