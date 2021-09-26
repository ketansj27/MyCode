'''
Tarrif ::
    units       Rs/unit
    0-100       5
    101-200     7
    201-300     10
    301--500    15
'''
unit = int(input())
if unit < 100:
    print(unit * 5)
elif unit < 200:
    print(100*5 + (unit -100)*7)
elif unit < 300:
    print(100*5 + 100*7 + (unit-200)*10)
elif unit < 500:
    print(100*5 + 100 *7 + 100 *10 + (unit-300)*15)