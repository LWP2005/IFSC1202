number = int(input("Enter First 2 Digit Number: "))
second = number // 10
first = number % 10

snumber = int(input("Enter Second 2 Digit Number: "))
ssecond = snumber // 10
sfirst = snumber % 10

thou = second * 1000
hund = ssecond * 100
ten = first * 10
sum = thou + hund + ten + sfirst
print("Merged Number:", sum)