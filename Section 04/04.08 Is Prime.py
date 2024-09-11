N = float(input("Enter N: "))

for i in range(2, N / 2 + 1):
    if i % N == 0:
        print("PRIME")
    else:
        print("COMPOSITE")