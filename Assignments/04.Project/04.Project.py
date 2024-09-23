start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))

for i in range(start, end + 1):
    isPrime = True
    for p in range(2, int(i/2 + 1)):
        if i % p == 0:
            isPrime = False
    if isPrime:
        print(i)