import random

def main():
    inputLevel=get_level()
    score=0
    for i in range(10):
        number1=generate_integer(inputLevel)
        number2=generate_integer(inputLevel)
        number=number1+number2
        n=0
        for tri in range(3):
            numberInput=input(f"{number1} + {number2} = ")
            if number==numberInput and numberInput.isdigit():
                score+=1
                break
            else:
                print('EEE')
                n+=1
                if n == 3:
                    print(f"{number1} + {number2} = {number}")
                    break
    print("Score:",score)

def get_level():
    while True:
        level = input('Level: ')
        if level.isdigit():
            level = int(level)
        else:
            continue
        if 1 <= level <= 3:
            return level
        else:
            continue
def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)

if __name__ == "__main__":
    main()