from datetime import date, datetime
import re
import sys
import inflect

def main():
    birth_date=input("Date of Birth: ")
    match=re.fullmatch("\d{4}-\d{2}-\d{2}",birth_date)
    if match:
        birth_date=datetime.strptime(birth_date,f"%Y-%m-%d")
        min=convert_to_min(birth_date)
        text=convert_to_text(min)
        print(text, "minutes")
    else:
        sys.exit("Invalid date")

def convert_to_min(birth):
    today=date.today()
    today=datetime.strptime(f"{today}",f"%Y-%m-%d")
    return ((today-birth).days)*24*60

def convert_to_text(min):
    text = inflect.engine()
    return text.number_to_words(min, andword="").capitalize()

if __name__ == "__main__":
    main()
