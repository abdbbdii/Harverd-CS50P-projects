# from datetime import date
# print((date.today()-date(2004, 1, 5)).days)
from datetime import datetime


lol=datetime.strptime("2002-12-12" ,"%Y-%m-%d")
print(lol)

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
date_object=datetime.strftime(date_object)
print("date_object =", date_object)