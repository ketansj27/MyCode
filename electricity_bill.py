'''
This code calculate energy bill based on tariff eCharge  of 'Mahavitaran' electricity
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
           
print("You intered your previous reading",previous_reading,"unit & current_reading as",current_reading,"unit.")
print("\n")
unit_consume = int(current_reading - previous_reading)
print("Units consumed :",unit_consume,"unit \n")

eCharge = float(0)
if unit_consume <= 100 :
    eCharge = 3.44 * unit_consume
elif unit_consume <= 300 :                                               # this are the different eCharges as per unit consumed.
    eCharge = (3.44*100)+(unit_consume-100)*7.34
elif unit_consume <= 500 :
    eCharge = (3.44*100)+(7.34*200)+(unit_consume-300)*10.36
elif unit_consume <= 1000:
    eCharge = (3.44*100)+(7.34*200)+(10.34*200)+(unit_consume-500)*11.82
elif unit_consume > 1000 :
    eCharge = (3.44*100)+(7.34*200)+(10.34*200)+(11.82*500)+(unit_consume-1000)*13.82
    
def computepay(eCharge,units):
    fix_charge = float(102)                                 # As per the 1 Apl 2021 - 31 Mar 202 Fixed Charges & Wheeling Charges are taken.
    W_charge = float(1.38) 
    return float(eCharge) + float(fix_charge) + float(W_charge)*int(units)

To_pay = int(computepay(eCharge,unit_consume))
print("Eelctricty bill :",To_pay,"Rs")
