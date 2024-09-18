def calculate_average():
    numbers = []

    print("Enter numbers (press Enter to finish):")
    
    while True:
        user_input = input()
        if user_input == "":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if len(numbers) == 0:
        print("Sequence Length is 0.")
    else:
        average = sum(numbers) / len(numbers)
        print(f"The average is: {average}")

calculate_average()