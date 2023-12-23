def main():
    time = convert(input("What time is it? ").strip())
    if (7.0 <= time <= 8.0):
        print("breakfast time")
    elif (12.0 <= time <= 13.0):
        print("lunch time")
    elif (18.0 <= time <= 19.0):
        print("dinner time")

def convert(temp):
    hrs, mins = temp.split(":")
    if mins.endswith("a.m.") or mins.endswith("p.m."):
        mins, add = mins.split(" ")
        if add == "a.m.".casefold():
            inc = 0.0
        else:
            inc = 12.0
    else:
        inc = 0
    temp = float(hrs)+float(mins)/60+float(inc)
    return temp

if __name__ == "__main__":
    main()