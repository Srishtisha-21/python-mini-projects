import random
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_title():
    print(Fore.CYAN + Style.BRIGHT + "\n🎯==========================================")
    print(Fore.MAGENTA + Style.BRIGHT + "        WELCOME TO THE NUMBER GUESSER!")
    print(Fore.CYAN + Style.BRIGHT + "==========================================🎯\n")

def choose_difficulty():
    print(Fore.YELLOW + "Choose your difficulty level:")
    print(Fore.GREEN + "1. Easy   (1–20)")
    print(Fore.BLUE + "2. Medium (1–100)")
    print(Fore.RED + "3. Hard   (1–500)")

    while True:
        choice = input(Fore.WHITE + "\nEnter 1, 2, or 3: ")
        if choice == '1':
            return 20
        elif choice == '2':
            return 100
        elif choice == '3':
            return 500
        else:
            print(Fore.RED + "⚠️ Invalid choice. Try again!")

def play_game():
    print_title()
    max_number = choose_difficulty()
    secret_number = random.randint(1, max_number)
    attempts = 0

    print(Fore.CYAN + f"\nI'm thinking of a number between 1 and {max_number}...")
    print(Fore.LIGHTBLACK_EX + "(Type a number and press Enter to guess!)\n")

    while True:
        try:
            guess = int(input(Fore.WHITE + "🔢 Your guess: "))
            attempts += 1

            if guess < secret_number:
                print(Fore.YELLOW + "📉 Too low! Try again.\n")
            elif guess > secret_number:
                print(Fore.YELLOW + "📈 Too high! Try again.\n")
            else:
                print(Fore.GREEN + Style.BRIGHT + f"\n🎉 You got it in {attempts} attempts!")
                print(Fore.MAGENTA + f"The secret number was {secret_number}.\n")
                break
        except ValueError:
            print(Fore.RED + "⚠️ Please enter a valid number!\n")

def play_again():
    while True:
        again = input(Fore.CYAN + "Do you want to play again? (y/n): ").lower()
        if again == 'y':
            print(Fore.MAGENTA + "\n🔁 Restarting the game...\n")
            time.sleep(1)
            play_game()
        elif again == 'n':
            print(Fore.GREEN + "\n👋 Thanks for playing! See you next time!")
            break
        else:
            print(Fore.RED + "Please enter 'y' or 'n'.")

if __name__ == "__main__":
    play_game()
    play_again()
