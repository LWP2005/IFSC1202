number = int(input("Enter a Number: "))
hund = number % 1000
tens = hund % 100
nnumb = tens // 10
print("Tens Digit:", nnumb)