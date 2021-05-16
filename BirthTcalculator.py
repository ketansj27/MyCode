from datetime import datetime
# "pip3 install python-dateut", if not installed
from dateutil import relativedelta


s_date = input("Enter your Birth Date {dd/mm/yyyy} - ")

print("\n")
try :
    f_date = datetime.strptime(s_date, "%d/%m/%Y")
except :
    print(" please inter birth date in (dd/mm/yyyy) format.")
    print("\n")
    exit()
#print(f_date)

b_date = datetime.strftime(f_date,"%d %B, %Y")
print("Birth Date : ",b_date)

c_date = datetime.now()
#print(c_date)
print("\n")
#This will find the difference between the two dates

difference = relativedelta.relativedelta(c_date, f_date)

print("from your birth time count is ...\n")
print(difference.years," years")
print(difference.months," months")
print(difference.days," days")
print(difference.hours," hours")
print(difference.minutes," minutes")
print(difference.seconds," seconds")
print(difference.microseconds," microseconds.")
