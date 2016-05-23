from lib.rollsetting import *
import random

def diceRange(die):
    print("Lowest side %d : Highest side %d" % (die.low, die.high))

def diceRoll(die):
    print("Roll: %d" % (random.randrange(die.low, die.high)))
