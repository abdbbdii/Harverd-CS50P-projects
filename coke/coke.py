insert = 0
amount = 50
while True:
    insert=int(input("Insert Coin: "))
    if insert == 25 or insert == 10 or insert == 5:
        amount=amount-insert
        if amount>0:
            print("Amount Due:",amount)
        if amount<0:
            print("Change Owed:",abs(amount))
            break
        elif amount==0:
            print("Change Owed:",amount)
            break
    else:
        print("Amount Due:",amount)