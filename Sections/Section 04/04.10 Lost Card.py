sum = 0

numofcards = int(input("Enter Number of Cards: "))
for i in range(1, numofcards + 1):
    sum = sum + i

sum2 = 0

for i in range(numofcards - 1):
    num = int(input("Enter Card: "))
    sum2 = sum2 + num

miss = sum - sum2
print("Missing Card:", miss)