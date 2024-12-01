import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'^<iframe.*embed/(\w+).*</iframe>$',s)
    if match:
        return f"https://youtu.be/{match.group(1)}"


if __name__ == "__main__":
    main()