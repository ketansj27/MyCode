from datetime import datetime
import time
from dateutil import relativedelta          #"pip3 install python-dateutil", if not installed

s_date = input("Enter your Birth Date {dd/mm/yyyy} - ")

print("\n")
try :
    f_date = datetime.strptime(s_date, "%d/%m/%Y")
except :
    print(" please inter birth date in (dd/mm/yyyy) format.")
    exit()

b_date = datetime.strftime(f_date,"%d %B, %Y")
print("Birth Date : ",b_date)

c_date = datetime.now()

#This will find the difference between the two dates
difference = relativedelta.relativedelta(c_date, f_date)

print("from your birth time count is ...\n")
print("> ",difference.years,"years")
time.sleep(0.3)
print("> ",difference.months,"months")
time.sleep(0.3)
print("> ",difference.days,"days")
time.sleep(0.3)
print("> ",difference.hours,"hours")
time.sleep(0.3)
print("> ",difference.minutes,"minutes")
time.sleep(0.3)
print("> ",difference.seconds,"seconds")
time.sleep(0.3)
print("> ",difference.microseconds,"microseconds.")
time.sleep(0.3)
