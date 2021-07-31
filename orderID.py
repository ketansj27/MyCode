'''
A company wishes to devise an order confirmation procedure. They plan to require an extra 
confirmation instead of simply auto-confirmation the order at the time it is placed. For 
this purpose, the system will generate a one-time password to be shared with the customer.
The customer who is placing the order has to enter that one-time password to confirm the 
order. The one-time password is generated for the enqueued orderID, as the product of the 
digits in this orderID.

Write an algorithm to find the one-time password for the order ID.

Input Format :
The input consists of an integer orderID representing the order ID of the enqueued order.

Output Format :
Print an integer representing the one-time password generated for the order ID.

Example

Input : 2342
Output : 48

Explanation
The product of 2,3,4 and 2 gives 48.
'''

def orderIDconF(orderId):
    mul = 1
    for digit in orderId :
        digit = int(digit)
        #print(digit)
        mul = int(mul * digit)

    return(mul)

orderId = int(input())
orderId = str(orderId)
result = orderIDconF(orderId)
print(result)



