num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 < num2 and num2 < num3:
    print(num1, num2, num3)
else:
    if num1 < num3 and num3 < num2:
        print(num1, num3, num2)

if num2 < num1 and num1 < num3:
    print(num2, num1, num3)
else:
    if num2 < num3 and num3 < num1:
        print(num2, num3, num1)

if num3 < num2 and num2 < num1:
    print(num3, num2, num1)
else:
    if num3 < num1 and num1 < num2:
        print(num3, num1, num2)