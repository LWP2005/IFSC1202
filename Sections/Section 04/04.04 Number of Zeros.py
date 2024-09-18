sum = 0

N = int(input("Enter N: "))
for i in range(N):
    num = int(input("Enter Number: "))
    if num == 0:
        sum = sum + 1

print("Number of Zeros:", sum)