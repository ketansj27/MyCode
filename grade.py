score = input("Enter score: ")
try :
    score = float(score)
except :
    print("error, inter numeric input")
    exit()

if score <= 1 :
    if score >= 0.9 :
        print("A")
    elif score >=0.8 :
        print("B")
    elif score >= 0.7 :
        print("C")
    elif score >= 0.6 :
        print("D")
    elif score < 0.6 :
        print("f")
else :
    print("error , plaese inter correct score")
    