"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        try:
            print(message)
            not_number_input = int(input())
        except Exception:
            pass
        else:
            break
        
    return not_number_input


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    number = not_number_rejector("Enter a number: ")
    while number < low or number > high:
        if number < low:
            print("Out of bounds, too low")
            number = not_number_rejector("Enter a number: ")
        else:
            print("Out of bounds, too high")
            number = not_number_rejector("Enter a number: ")
    
    return number

def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    lowerbound = not_number_rejector("Enter low bound: ")
    upperbound = not_number_rejector("Enter upper bound: ")
    actualNumber = random.randint(lowerbound, upperbound)
    guessed = False
    while not guessed:
      guessedNumber = super_asker(lowerbound,upperbound)
      if guessedNumber == actualNumber:
        guessed = True
      elif guessedNumber < actualNumber:
        print("Too low, try again")
      else:
        print("Too high, try again")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
