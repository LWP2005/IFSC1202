number = int(input("Enter Four Digit Number: "))
thou = number // 1000
hund = (number % 1000) // 100
ten = ((number % 1000) % 100) // 10
one = (number % 1000) % 10

if thou == one and hund == ten:
    print("YES")
else:
    print("NO")