number = int(input("Enter a 3 Digit Number: "))
third = number // 100
second = (number % 100) // 10
first = (number % 100) % 10
sum = third + second + first
print("Sum of Digits:", sum)