'''
In this code you can convert decimal/int numbers into binary, hexa, octal bu using in_built fuctions
'''

digit = int(input("Enter a decimal number: "))

binary = bin(digit).replace("0b","")
hexa = hex(digit).replace("0x","")
octal = oct(digit).replace("0o","")

print("binary      ",binary)
print("hexadecimal ",hexa)
print("octal       ",octal)
