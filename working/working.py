import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.fullmatch(
        r"(\d{1,2}(?::\d{1,2})?) (AM|PM) to (\d{1,2}(?::\d{1,2})?) (AM|PM)", s
    ):
        if match.group(1).find(":") != -1:
            hh1, mm1 = match.group(1).split(":")
            if hh1 == "12":
                hh1 = f"{int(hh1)-12}"
            if int(mm1) >= 60:
                raise ValueError
            if match.group(2) == "PM":
                hh1 = f"{int(hh1)+12}"
            if match1 := re.fullmatch(r"(\d)", hh1):
                hh1 = f"0{match1.group(1)}"
            time1 = f"{hh1}:{mm1}"
        else:
            time1 = match.group(1)
            if time1 == "12":
                time1 = f"{int(time1)-12}"
            if match.group(2) == "PM":
                time1 = int(time1)
                time1 = f"{time1+12}"
            if match1 := re.fullmatch(r"(\d)", time1):
                time1 = f"0{match1.group(1)}"
            time1 = f"{time1}:00"
        if match.group(3).find(":") != -1:
            hh2, mm2 = match.group(3).split(":")
            if hh2 == "12":
                hh2 = f"{int(hh2)-12}"
            if int(mm2) >= 60:
                raise ValueError
            if match.group(4) == "PM":
                hh2 = f"{int(hh2)+12}"
            if match2 := re.fullmatch(r"(\d)", hh2):
                hh2 = f"0{match2.group(1)}"
            time2 = f"{hh2}:{mm2}"
        else:
            time2 = match.group(3)
            if time2 == "12":
                time2 = f"{int(time2)-12}"
            if match.group(4) == "PM":
                time2 = int(time2)
                time2 = f"{time2+12}"
            if match2 := re.fullmatch(r"(\d)", time2):
                time2 = f"0{match2.group(1)}"
            time2 = f"{time2}:00"
        return f"{time1} to {time2}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()