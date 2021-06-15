# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

number = random.randint(1, 100)

print("Welcome the the Number Guessing Game! \nI'm thinking of a number between 1 and 100.\n")

print(f"Psst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "hard":
    lives = 5
elif difficulty == "easy":
    lives = 10
else:
    print("You have entered an invalid difficulty")


def game(level):
    end_of_game = False
    global lives
    print(f"You have {lives} attempts remaining to guess the number")

    while not end_of_game:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}")
            end_of_game = True
        elif guess > number:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You've run out of guesses, you lose.")
            print("Too high.")
            if lives > 0:
                print(f"You have {lives} attempts remaining to guess the number")
                # print("Guess again.")
        elif guess < number:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You've run out of guesses, you lose.")
            print("Too low.")
            if lives > 0:
                print(f"You have {lives} attempts remaining to guess the number")
                # print("Guess again.")


game(difficulty)


