def main():
    while True:
        try:
            userInput = input("Fraction: ")
            print(gauge(convert(userInput)))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    a, b = fraction.split("/")
    value = ((int(a)/int(b))*100)
    return round(value,)

def gauge(percentage):
    if 5 >= percentage >= 0:
        return "E"
    elif 95 <= percentage <= 100:
        return "F"
    elif percentage > 100:
        raise ValueError
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()