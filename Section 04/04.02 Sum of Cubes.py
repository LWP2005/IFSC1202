sum = 0

N = int(input("Enter N: "))
for i in range(1, N + 1):
    sum = sum + (i ** 3)
print(sum)