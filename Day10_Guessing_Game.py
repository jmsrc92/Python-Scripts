import random

print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

random_number = random.randint(1, 100)

guesses_left = 0

if difficulty == "easy":
    guesses_left = 10
else:
    guesses_left = 5


def check_guess(player_guess):
    global random_number
    if player_guess == (random_number):
        return True
    elif player_guess > random_number:
        print("Too high \nGuess again")
        return False
    elif player_guess < random_number:
        print("Too low \nGuess again")
        return False
    else:
        return False


while guesses_left > 0:
    print(f"You have {guesses_left} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if check_guess(guess):
        print("You guessed correctly")
        guesses_left = 0
    else:
        guesses_left -= 1
