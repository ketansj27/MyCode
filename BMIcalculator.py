# -*- coding: utf-8 -*-

while True :
    try :
        weight = int(input("Enter your weight in Kg : "))
        height = float(input("Enter your height in cm : "))
        break
    except :
        print("value error ! 'Not number'")

bmi = weight/height/height*10000
print("\n* Your BMI is ",round(bmi,2),"Kg/m^2")


def comments(bmi,h):
    h = h/100
    l_weight = h*h * 18.5
    H_weight = h*h * 24.5
    print(" \n According to the height, your Weight should be in rage of ",
          round(l_weight,2),"Kg "" To ",round(H_weight,2),"Kg")
print("\n")

# determine the BMI
if bmi < 18.5 :
    print("__Under weight__")
    comments(bmi,height)
elif bmi >18.5 and bmi <= 24.9 :
     print("__Normal weight__\n")
     print("According to Height, your Weight is GOOD !")
elif bmi > 24.9 and bmi <= 29.9 :
    print("__Over weight__")
    comments(bmi,height)
else :
    print("__Obesity__")
    comments(bmi,height)

