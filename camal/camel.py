camelCase = input("camelCase: ")
for i in camelCase:
    if i.isupper():
        camelCase = camelCase.replace(i, "_" + i.lower())
print("snake_case:", camelCase)