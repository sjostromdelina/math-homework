import random

def play_game():
    # Generate a random number between 1 and 10
    number = random.randint(1, 10)
    
    # Ask the user to guess the number
    guessed = False
    while not guessed:
        try:
            guess = int(input("Guess the number: "))
            if guess < number:
                print("Too low. Guess again.")
            elif guess > number:
                print("Too high. Guess again.")
            else:
                guessed = True
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    play_game()
