months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        userInput=input("Date: ").strip()
        if userInput.find('/') != -1:
            mm,dd,yyyy=userInput.split("/")
            mm=int(mm)
        elif userInput.find(', ') != -1:
            mmmmdd,yyyy=userInput.split(", ")
            mmmm,dd=mmmmdd.split(" ")
            if mmmm in months:
                mm = int(months.index(mmmm))+1
        dd=int(dd)
        if (1 <= mm <= 12) and (1 <= dd <= 31):
            print(f"{yyyy}-{mm:02}-{int(dd):02}")
        else:
            continue
    except (NameError, ValueError):
        pass
    else:
        break