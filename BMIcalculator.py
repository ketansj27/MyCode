# -*- coding: utf-8 -*-

class valueError1(UserWarning):
    pass
class valueError2(UserWarning):
    pass

while True :
    try :
        weight = float(input("Enter your weight in Kg : "))
        height = float(input("Enter your height in cm : "))
        bmi = weight/height/height*10000
        if bmi > 40 :
            print("BMI = ",round(bmi,2))
            raise valueError1
        elif bmi < 8 :
            print("BMI = ",round(bmi,2))
            raise valueError2
        break

    except valueError1 :
        print("\n'Invalid Data', BMI is greater than 40\n")
    except valueError2 :
        print("\n'Invalid Data', BMI is smaller than 8\n")
    except :
        print("value error ! 'Not number'")

print("\n* Your BMI is ",round(bmi,2),"Kg/m^2")

def comments(bmi,h):
    h = h/100
    l_weight = h*h * 18.5
    H_weight = h*h * 24.5
    print(" \n According to the height your Weight should be in rage of ",
          round(l_weight,2),"Kg "" To ",round(H_weight,2),"Kg")
print("\n")

# determine the BMI
if bmi < 18.5 :
    print("__Under weight__")
    comments(bmi,height)
elif bmi >18.5 and bmi <= 24.9 :
     print("__Normal weight__\n")
     print("According to Height your Weight is GOOD !")
elif bmi > 24.9 and bmi <= 29.9 :
    print("__Over weight__")
    comments(bmi,height)
else :
    print("__Obesity__")
    comments(bmi,height)
