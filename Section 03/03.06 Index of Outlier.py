print("Enter Three Numbers, Two Being the Same and the Last Being Different:")
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 == num2:
    print("The Outlier is the Third Number")
else:
    if num2 == num3:
        print("The Outlier is the First Number")
    else:
        print("The Outlier is the Second Number")