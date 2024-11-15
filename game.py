import random

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "You lose!"

def display_scores(user_score, computer_score):
    print("\n--- Current Scores ---")
    print(f"User: {user_score}")
    print(f"Computer: {computer_score}")

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = input("\nEnter your choice (Rock, Paper, Scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        display_scores(user_score, computer_score)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Final scores:")
            display_scores(user_score, computer_score)
            break

if __name__ == "__main__":
    main()
