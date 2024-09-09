num = int(input("Enter N: "))
for i in range(1, num + 1):
    for i in range(1, i + 1):
        print(i, sep="", end="")
    print("")