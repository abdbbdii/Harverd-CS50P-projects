names = []
while True:
    try:
        userInput = input().strip()
        names.append(userInput)
    except EOFError:
        if len(names) == 0:
            continue
        else:
            break

if len(names) >= 1:
    print("Adieu, adieu, to ", end="")
    if len(names) == 1:
        print(f"{names[0]}")
    if len(names) == 2:
        print(f"{names[0]} and {names[1]}")
    if len(names) > 2:
        for i in range(len(names[:-1])):
            print(f"{names[i]}", end=", ")
        print(f"and {names[-1]}")
