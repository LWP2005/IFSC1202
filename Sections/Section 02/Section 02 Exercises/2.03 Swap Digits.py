number = int(input("Enter Number: "))
firstdigit = number % 10
seconddigit = number // 10
tens = firstdigit * 10
swappednumber = tens + seconddigit
print("Swapped Number:", swappednumber)