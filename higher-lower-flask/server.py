from flask import Flask
app = Flask(__name__)
import random

number = random.randint(0, 9)
print(number)

@app.route('/')
def home():
    return 'Guess a number between 0 and 9'


@app.route('/<int:guess>')
def answer(guess):

    if number == guess:
        return 'Correct!'
    elif guess < number:
        return 'Too low'
    elif guess > number:
        return 'Too high'




app.run(debug=True)