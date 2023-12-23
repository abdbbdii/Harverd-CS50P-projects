def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) <=6 and len(s) >=3 and s[0:2].isalpha() and s.isalnum() and isZero(s) and isMiddle(s):
        return True

def isZero(s):
    if s.find('0') != -1:
        for element in s:
            if element.isalpha():
                if s[s.index(element)+1]=='0':
                    return False
            else:
                return True
    else:
        return True

def isMiddle(s):
    for element in s:
        if element.isdigit() and not s.isalpha():
            if s[s.index(element):].isdigit():
                return True
            else:
                return False

        elif s.isalpha():
            return True

main()