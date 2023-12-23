import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match=re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)",ip)
    if match:
        if 0 <= int(match.group(1)) <= 255 and 0 <= int(match.group(2)) <= 255 and 0 <= int(match.group(3)) <= 255 and 0 <= int(match.group(4)) <= 255:
            return True
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    main()