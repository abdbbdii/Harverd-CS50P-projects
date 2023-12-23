from validator_collection import validators, errors
try:
    if validators.email(input("What's your email address? ")):
        print("Valid")
    else:
        print("Invalid")
except errors.InvalidEmailError:
    print("Invalid")