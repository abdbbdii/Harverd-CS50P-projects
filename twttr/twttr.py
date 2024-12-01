string = input("Input: ")
for element in string:
    if (
        element == "a"
        or element == "e"
        or element == "i"
        or element == "o"
        or element == "u"
        or element == "A"
        or element == "E"
        or element == "I"
        or element == "O"
        or element == "U"
    ):
        string = string.replace(element, "")
print("Output:", string)