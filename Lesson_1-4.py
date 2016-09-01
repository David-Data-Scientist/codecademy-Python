# Single line comment:
# context


# Multiple line comment:
"""
context
"""


# String method:
str(context)
len(context)

something.upper()  # Return characters with uppercase
something.lower()  # Return characters with lowercase


# Print method:
meal = 44.50
tax = 0.0675
tip = 0.15
meal += meal * tax
total = meal + meal * tip
print("%.2f" % total)  # Return 2 decimal point

g = "Golf"
h = "Hotel"
total = 13.4 * 0.12
print("%s, %s" % (g, h))  # Return string type


# Datetime library:
"""from datetime import datetime"""
now = datetime.now()
print('%s/%s/%s %s:%s:%s' % (now.year, now.month, now.day,  # Print year/month/day etc in string format
                             now.hour, now.minute, now.second))


# Order of logic:
"""not > and > or"""

bool_one = (2 <= 2) and "Alpha" == "Bravo"  # Make me false!

bool_two = (2 <= 2) and not "Alpha" == "Bravo"  # Make me true!

bool_three = not (2 <= 2) and not "Alpha" == "Bravo"  # Make me false!

bool_four = not (2 <= 2) or not "Alpha" == "Bravo"  # Make me true!

bool_five = (2 <= 2) or "Alpha" == "Bravo"  # Make me true!


# if statement:


def the_flying_circus():  # Make sure that the_flying_circus() returns True
    if not 1 < 3:
        return True
    elif 1 < 3:
        return True
    else:
        return False


'''###################################Playing a game################################################'''
"""
Pig Latin is a language game, where you move the first letter of the word to the end and add "ay."
So "Python" becomes "ythonpay." To write a Pig Latin translator in Python, here are
the steps we'll need to take:

Ask the user to input a word in English.
Make sure the user entered a valid word.
Convert the word from English to Pig Latin.
Display the translation result.
"""

pyg = 'ay'
original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
    word = original.lower()
    new_word = word[1:len(word)] + pyg
    print(new_word)
else:
    print('empty')


# Building functions:


def cube(number):
    return number ** 3


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return "Nope"


# Import module:
"""
from math import sqrt  # Only import sqrt() method
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!
"""

"""
two ways of using sqrt:
from math import sqrt
print sqrt(13689)
OR:
import math
print math.sqrt(13689)
"""

# Built-in functions:
max()
min()
abs(value)
type(value)


'''###############################Taking a Vacation Exercise##########################################'''

# Build some functions to calculate the cost for a vacation


def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angles":
        return 475


def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif 3 <= days < 7:
        return 40 * days - 20
    else:
        return 40 * days


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

"""What if we went to Los Angles for 5 days and brought an extra 600 dollars of spending money?"""
trip_cost("Los Angles", 5, 600)
