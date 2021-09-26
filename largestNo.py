# find largest no from string of continous-numbers.

digits = input()

largest_Yet = -1
for num in digits:
    num = int(num)
    if num > largest_Yet:
        largest_Yet = num
print(largest_Yet)

