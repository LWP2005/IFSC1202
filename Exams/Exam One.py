#prompt
user_name = input("Hello! What is your name? ")
print(f"Well, {user_name}, I am thinking of a number between 1 and 20.")
print("You have 5 guesses.")

#random number
from random import randint
random_num = randint(1,20)

#game starts and range is the rounds.
for i in range(1, 5 + 1):
    user_guess = int(input("Take a guess. "))
    
    #correct guess
    if user_guess == random_num:
        if i == 1:
            print(f"Good job, {user_name}! You guessed my number in {i} guess!")
        else:
            print(f"Good job, {user_name}! You guessed my number in {i} guesses!")
        break
    
    #guess is too high
    if user_guess > random_num:
        print("Your guess is too high.")
    
    #guess is too low
    if user_guess < random_num:
        print("Your guess is too low.")

#after number of guesses have been all used up
if i == 5:
    print(f"Nope. The number if was thinking of was {random_num}")