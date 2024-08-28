number = int(input("Enter a 3 Digit Number: "))
third = number // 100
second = (number % 100) // 10
first = (number % 100) % 10
nfirst = first * 100
nsecond = second * 10
sum = nfirst + nsecond + third
print("Reverse of Digits:", sum)