month = int(input("Enter Month: "))
day = int(input("Enter Day: "))

if month == 4 or month == 6 or month == 9 or month == 11 and day < 30:
    print(month, "/", day + 1)
else:
    if month == 4 or month == 6 or month == 9 or month == 11 and day == 30:
        print(month + 1, "/", 1)
    else:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and day < 31:
            print(month, "/", day + 1)
        else:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and day == 31:
                print(month + 1, "/", 1)
            else:
                if month == 2 and day < 28:
                    print(month, "/", day + 1)
                else:
                    if month == 2 and day == 28:
                        print(month + 1, "/", 1)