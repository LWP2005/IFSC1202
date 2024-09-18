number = int(input("Enter a 3 Digit Number: "))
third = number // 100
second = (number % 100) // 10
first = (number % 100) % 10

if third < second and second < first:
    print("YES")
else:
    print("NO")