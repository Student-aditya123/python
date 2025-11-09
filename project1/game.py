import random

# Optional: colorama for colorful text
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR = True
except ImportError:
    COLOR = False

# Choices and winning rules
choices = ["snake", "water", "gun"]
winning_cases = {"snake": "water", "water": "gun", "gun": "snake"}

# Function: speak message (reinitializes engine each time)
def say_message(message):
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        engine.say(message)
        engine.runAndWait()
        engine.stop()
    except Exception:
        pass  # if pyttsx3 isn't installed or fails, skip voice

# Function: get user input
def get_user_choice():
    while True:
        choice = input("Enter your choice (snake, water, gun): ").lower()
        if choice in choices:
            return choice
        else:
            if COLOR:
                print(Fore.RED + "Invalid choice! Try again.")
            else:
                print("Invalid choice! Try again.")

# Function: get computer choice
def get_computer_choice():
    return random.choice(choices)

# Function: decide winner
def decide_winner(user, computer):
    if user == computer:
        return "draw"
    elif winning_cases[user] == computer:
        return "user"
    else:
        return "computer"

# Main game
def play_game():
    user_score = 0
    computer_score = 0
    history = []

    welcome_msg = "\nWelcome to Snake, Water, Gun!\nFirst to 5 points wins.\n"
    if COLOR:
        print(Fore.CYAN + welcome_msg)
    else:
        print(welcome_msg)
    say_message("Welcome to Snake, Water, Gun game! First to five points wins. Let's start!")
    say_message("before starting this game I tell you that this game designed by Aditya")

    while user_score < 5 and computer_score < 5:
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"Computer chose: {computer}")

        winner = decide_winner(user, computer)
        history.append((user, computer, winner))

        if winner == "user":
            user_score += 1
            msg = "🎉 You win this round!"
            if COLOR:
                print(Fore.GREEN + msg)
            else:
                print(msg)
            say_message("Yeee, you win this round!")
        elif winner == "computer":
            computer_score += 1
            msg = "Computer wins this round!"
            if COLOR:
                print(Fore.RED + msg)
            else:
                print(msg)
            say_message("Oh no, computer wins this round!")
        else:
            msg = "This round is a draw!"
            if COLOR:
                print(Fore.BLUE + msg)
            else:
                print(msg)
            say_message("It's a draw!")

        print(f"Score -> You: {user_score}, Computer: {computer_score}\n")

    # Final Result
    print("\nGame Over!")
    if user_score > computer_score:
        final_msg = "🎉 Congratulations! You won the game!"
        if COLOR:
            print(Fore.GREEN + final_msg)
        else:
            print(final_msg)
        say_message("Congratulations! You won the game!")
    else:
        final_msg = "💻 Computer won the game! Better luck next time."
        if COLOR:
            print(Fore.RED + final_msg)
        else:
            print(final_msg)
        say_message("Computer won the game! Better luck next time.")

    # Show history
    print("\nGame History (Your choice, Computer choice, Winner):")
    for idx, h in enumerate(history, 1):
        u, c, w = h
        print(f"Round {idx}: {u} vs {c} -> {w}")

# Run the game
if __name__ == "__main__":
    play_game()
