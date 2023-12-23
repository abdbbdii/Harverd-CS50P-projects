ans = input ("What is the Answer to the Great Question of Life, the Universe and Everything? ").casefold().strip()
if ans == "forty two" or ans == "forty-two" or ans == "42":
    print("Yes")
else:
    print("No")