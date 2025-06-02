import random

# Loop
while True:
# If yser enters y
    choice = input("Roll the dice? (y/n): ").lower()
#Ask: roll the dice?
    if choice == "y":
# Generate two random numbers    
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
#Print them     
        print(f"({dice1}, {dice2})")
# If user enters n
    elif choice == "n":
# Print thank you message     
        print("Thank you for playing!")
#Terminate 
        break
    else:
        print("Invalid choice!")





#Else
#Print invalid choice