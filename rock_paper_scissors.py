import random
choices = ("r", "p", "s")

while True:
    user_choice = input("Rock, Paper, or scissors (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice!")
    computer_choice = random.choice(choices)
    print(f"You {user_choice}")
    print(f"Computer chose {computer_choice}")
print('')




#Ask the user to make a choice
#If choice is not valid 
# Print an error
# Let the computer to make a choice
# Print choices (emohis)
#Determine the winner
#Ask the user if they want to continue 
#If not 
#Terminate