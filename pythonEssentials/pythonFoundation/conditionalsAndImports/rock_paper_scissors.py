import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("Enter your choice (rock, paper, scissors): \n").lower()

if computer_choice == user_choice:
     print(f"Both chose {computer_choice}. It's a tie!\n")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'paper' and computer_choice == 'rock') or \
     (user_choice == 'scissors' and computer_choice == 'paper'):
     print(f"You chose {user_choice}, computer chose {computer_choice}. You win!\n")
else:    
     print(f"You chose {user_choice}, computer chose {computer_choice}. Computer wins!\n")