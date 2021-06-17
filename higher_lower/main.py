from art import logo
import os
from art import vs
from game_data import data
import random

os.system('clear')
print(logo)

score = 0
is_game_over = False

while not is_game_over:

    compare1 = random.choice(data)

    name1 = compare1["name"]
    count1 = compare1["follower_count"]
    description1 = compare1["description"]
    country1 = compare1["country"]

    print(f"Compare A: {name1}, a {description1}, from {country1}")

    print(vs)

    compare2 = random.choice(data)

    name2 = compare2["name"]
    count2 = compare2["follower_count"]
    description2 = compare2["description"]
    country2 = compare2["country"]

    print(f"Against B: {name2}, a {description2}, from {country2}")

    selection = input("Who has more followers? Type 'A' or 'B' ")
    selection.lower()

    if selection == "a":
        if count1 > count2:
            os.system('clear')
            print(logo)
            score = score + 1
            print(f"You\'re right! Current score: {score}")
            is_game_over = False
        else:
            os.system('clear')
            print(logo)
            print(f"Sorry, that\'s wrong. Final score: {score}")
            is_game_over = True
    elif selection == "b":
        if count2 > count1:
            os.system('clear')
            print(logo)
            score = score + 1
            print(f"You\'re right! Current score: {score}")
            is_game_over = False
        else:
            os.system('clear')
            print(logo)
            print(f"Sorry, that\'s wrong. Final score: {score}")
            is_game_over = True


