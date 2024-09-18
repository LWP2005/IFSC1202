total_sum = 0

while True:
    
    user_input = input("Enter Number (CR to Quit): ")

    if user_input == "":
        break
    
    try:
        number = int(user_input)
        total_sum = total_sum + number
    
    except ValueError:
        print("Value Error")

print("The Total Sum:", total_sum)