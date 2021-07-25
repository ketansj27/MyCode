
# method to compute gcd ( recursion )

def hcf(num1,num2):
	if(num2 == 0):
		return num1
	else:
		return hcf(num2, num1 % num2)

num1 = int(input("Inter Number-1 : "))
num2 = int(input("Inter Number-2 : "))

gcd = hcf(num1, num2)
print("The gcd of",num1," and ",num2," is : ",gcd)

