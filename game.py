import random

choices = ['rock', 'paper', 'scissors']
win_map = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
lose_map = {v: k for k, v in win_map.items()} # reverse the win_map

print("Welcome to Rock, Paper, Scissors!")
difficulty = input("Choose difficulty (easy/ normal / hard): ").strip().lower()
while difficulty not in ['easy', 'normal', 'hard']:
    difficulty = input("Please type easy, normal, or hard: ").strip().lower()


wins = losses = ties = 0

def _get_computer_choice(user_choice):
    if difficulty == 'easy':
        #Computer tends to lose
        return win_map[user_choice] if random.random() < 0.7 else random.choice(choices)
    elif difficulty == 'hard':
        #Computer tends to win
        return lose_map[user_choice] if random.random() < 0.7 else random.choice(choices)
    else:
        #Normal: pure random
        return random.choice(choices)


while True:
    user_choice = input("Choose rock, paper, or scissors (or type 'quit' to stop): ").strip().lower()

    if user_choice == 'quit':
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice. Try again.\n")
        continue

    computer_choice = random.choice(choices)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!\n")
        ties += 1
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!\n")
        wins += 1
    else:
        print("Computer wins!\n")
        losses += 1

    print(f"Score — Wins: {wins}, Losses: {losses}, Ties: {ties}\n")
