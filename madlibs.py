"""A madlib game that compliments its users."""

from random import choice
import re
from turtle import color

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)



@app.route('/game')
def show_madlib_form():
        answer = request.args.get("game")

        if answer == 'no':
            return render_template("goodbye.html")
        elif answer == 'yes':
            return render_template("game.html")


@app.route('/madlib')
def show_madlib():
        person = request.args.get("person")
        color = request.args.get("color")
        noun = request.args.get("noun")
        adjective = request.args.get("adjective")

        return f"""
        <!doctype html>
        <html>
        <head>
        <title>MADLIB</title>
        </head>
        <body>
            There once was a { color } { noun } sitting in the Computer Lab.
            When { person } went to pick it up, it burst into flames in a totally
            { adjective } way.
        </body>
        </html>
        """


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
