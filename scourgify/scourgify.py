import csv
import sys
import functions

First = []
Last = []
House = []
functions.sysMinMax(3)
functions.extension(".csv")
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            y, x=row['name'].split(', ')
            First.append(x)
            Last.append(y)
            House.append(row['house'])

    with open(sys.argv[2], "w") as file:
        fieldnames=['first','last','house']
        writer=csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(First)):
            writer.writerow(
                {
                    "first": First[i],
                    "last": Last[i],
                    "house": House[i],
                }
            )
except:
    sys.exit("File does not exist")
