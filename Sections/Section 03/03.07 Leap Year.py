year = int(input("Enter Four Digit Year: "))

if (year % 400) == 0:
    print("Leap Year")
else:
    if (year % 4) == 0:
        print("Leap Year")
    else:
        print("Common Year")