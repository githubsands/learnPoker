
import numpy as np
import numpy as chararray
import itertools as combinations

# ranks defines a 13x1 matrix - all possible ranks within the game of poker
def ranks(): 
    ranks = np.chararray((8, 1))
    ranks = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
    return ranks

# suites defines a 4x1 matrix - all possible suites within the game of poker
def suites():
    suites = np.chararray((4, 1))
    suites = ["diamonds", "hearts", "jacks", "clubs"]
    return suites

'''
def allPossibleCards(): 
    suites = suites()
    ranks = ranks()
    cards = np.chararray((4, 13))

    for i in range(0, 13):
        for j in range(0, 4):
            cards[i,j]= ranks[0,0] + suites[0,0]

    return
'''

def possibleStartingHands():
    return 1326
