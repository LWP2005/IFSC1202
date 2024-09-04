num1 = float(input("Enter First Number: "))
operation = input("Enter Operator (+, -, *, /): ")
num2 = float(input("Enter Second Number: "))

if operation == "+":
    print(num1, operation, num2, "=", num1 + num2)
else:
    if operation == "-":
        print(num1, operation, num2, "=", num1 - num2)
    else:
        if operation == "*":
            print(num1, operation, num2, "=", num1 * num2)
        else:
            if operation == "/":
                print(num1, operation, num2, "=", num1 / num2)
            else:
                print("Invalid Operator")