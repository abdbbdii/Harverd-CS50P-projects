def main():
    print("Output:",shorten(input("Input: ")))

def shorten(word):
    for i in word:
        if (
            i == "a"
            or i == "e"
            or i == "i"
            or i == "o"
            or i == "u"
            or i == "A"
            or i == "E"
            or i == "I"
            or i == "O"
            or i == "U"
        ):
            word = word.replace(i, "")
    return word

if __name__ == "__main__":
    main()