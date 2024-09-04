month = int(input("Enter Number of Month: "))

if month == 4 or month == 6 or month == 9 or month == 11:
    print("30 Days")
else:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("31 Days")
    else:
        print("28 Days")