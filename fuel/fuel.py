while True:
    try:
        a, b = input("Fraction: ").split("/")
        value = ((int(a)/int(b))*100)
        value = round(value,)
        if 5 >= value >= 0:
            print("E")
        elif 95 <= value <= 100:
            print("F")
        elif value > 100:
            continue
        else:
            print(f"{value}%")
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break