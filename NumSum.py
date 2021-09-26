numSize = input()
nums = str(input())
Asum = list()
nums = nums.replace(" ","")
sum = 0
for num in nums :
    sum = sum + int(num)
    #print(sum)
    Asum.append(sum)
print(*Asum,sep =" ")
