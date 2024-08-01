import random
choices = ["Rock", "Paper", "Scissors"]
computer_choice=random.choice(choices)
user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
while user_choice not in ["Rock", "Paper", "Scissors"]:
    user_choice = input("Invalid choice. Please enter Rock, Paper, or Scissors: ")
print(user_choice,computer_choice)
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):print("You win!")
else:
        print("Computer wins!")
