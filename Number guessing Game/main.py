import random

def print_divider():
    print("="*50)

def guessing_game():
    print_divider()
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 10.")
    print("Try to guess the number.")
    print_divider()

    n = random.randint(1, 10)
    guess = None
    points = 100

    while guess != n:
        guess = int(input("\nEnter your guess (between 1 and 10): "))
        
        if guess < 1 or guess > 10:
            print("Your guess is out of bounds! Please guess a number between 1 and 10.")
        elif guess < n:
            points *= 0.8
            print("Too low! Try again.")
        elif guess > n:
            points *= 0.8
            print("Too high! Try again.")
        else:
            print_divider()
            print("Congratulations! You guessed it right!")
            print(f"You scored {points:.2f} points.")
            print_divider()
            break

    print("\nThank you for playing the Number Guessing Game!")
    print_divider()

# Start the game
guessing_game()
