'''
This code calculate energy bill based on tariff rate  of 'Mahavitaran' electricity
board.( valid => 1 Apl, 2021 - 31 March, 2022)
'''
class NotPositiveError(UserWarning): 
    pass
class valueError(UserWarning):
    pass

while True:
    try:
        previous_reading = int(input("Enter previous reading (unit): "))
        current_reading = int(input("Enter current reading (unit): "))
    except:
        print("wrong Input 'Not Numbers', please try again.")
        continue
    try:
        if previous_reading <= 0:
            raise NotPositiveError
        elif current_reading <= 0:
            raise NotPositiveError
        break
    except NotPositiveError:
        print("Entered number was not positive, please try again.")
        
         
print("\n")
print("previous reading = ",previous_reading," unit")
print("current reading =",current_reading," unit")
print("\n")
unit_consume = int(current_reading - previous_reading)
print("Units consumed :",unit_consume,"unit \n")

rate = float(0)
if unit_consume <= 100 :
    rate = 3.44
elif unit_consume <= 300 :          # this are the different rates as per unit consumed.
    rate = 7.34
elif unit_consume <= 500 :
    rate = 10.36
elif unit_consume <= 1000:
    rate = 11.82
elif unit_consume > 1000 :
    rate = 11.82
    
print("According to unit consume, rate is ",rate,"Rs/unit \n")

def computepay(rate,units):
    fix_charge = float(102).         # According to 31 Apl - 31 Mar Fixed Charges & Wheeling Charges are taken.
    W_charge = float(1.38) 
    return float(rate) * int(units) + float(fix_charge) + float(W_charge)*int(units)

To_pay = int(computepay(rate,unit_consume))
print("Eelctricty bill is ",To_pay,"Rs")
