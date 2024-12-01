import re


def main():
    print(count(input("Text: ")))


def count(s):
    match=re.findall(r"\bum\b",s,re.IGNORECASE)
    return len(match)

if __name__ == "__main__":
    main()