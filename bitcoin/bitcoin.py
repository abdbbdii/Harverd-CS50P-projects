import requests
import sys

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    value = float((r["bpi"]["USD"]["rate"]).replace(",", "")) * float(sys.argv[1])
    print(f"${value:,.4f}")
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
