grocery = {}
while True:
    try:
        item=input().strip().upper()
        if item in grocery:
            grocery[item]+=1
        else:
            grocery[item]=1
    except EOFError:
        break
sortedGrocery=sorted(grocery)
for i in sortedGrocery:
    print(f"{grocery[i]} {i}")