import random

roll = random.randint(1, 6)

guess = int(input("Guess the dice roll (1-6): \n"))
if guess == roll:
     print("Congratulations! You guessed the correct number.")
else:    
     print(f"Sorry, the correct number was {roll}. Better luck next time!")