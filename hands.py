#!/usr/bin/env python

def HANDS():
    hands = ["straight flush", "four of a kind", "full house", "flush", "straight", "three of a kind", "two pair", "one pair", "high card"]
    return hands

def HAND_ODDS(): 
    hands = {"straight flush": 649740,
    "four of a kind": 4165, 
    "full house": 693, 
    "flush": 508, 
    "straight": 254, 
    "three of a kind": 46.3,
    "two pair": 21, 
    "one pair": 1.37, 
    "no pair": 17.4, }
    return hands

def HAND_PROBABILITIES():
    probabilities = {"straight flush":0.00139, 
                   "four of a kind":0.0240, 
                   "full house":0.1441, 
                   "flush":0.1965, 
                   "straight":0.3925,
                   "three of a kind":2.1128, 
                   "two pair":4.7539, 
                   "one pair":42.2569, 
                   "high card":50.1177,
                   "no pair": 4.74, }
    return probabilities


def printHands():
    hands = HANDS()
    for x in hands:
        print(str(hands.index(x))+":"+x)

# TOTALBURNTCARDS = 

# Worth it to count how many hands you have played?

# What hands are possible with this layout 
# I have this hand, what are the odds they have the other hand

# understand the difference of odds and probabiltiy of getting 
# probability: fraction of times you expect to see the event 
# odds: (probaiblity that event will occur/divided by probability that event will not occur)

# each game of poker is dependent on the past.  Each outcome is not truly random and does not consist of independent trials of 
# a random process" 
#
# gamblers fallacy arises from the belief of the law of small numbers. Leads to the erroneous belief that small samples must be 
# representative of the larger population
#
# gambler fallacy: a cognitive bias produced by a psychological heuristic called the representativeness heuristic
#
# insensitivity to sample size
# streaks occur in a small sample size
# 
# metagame and your hand are a reflexive process
# mistaken belief of internal locus of control 
# chance can overcome skill or talent
#
# do not underestimate how any observations are needed to detect a favorable outcome
# 
# for evens with a high degree of randomness detecting a bias that will lead to a favorable outcome takes an impractically large amount of time and is verify difficult

# goes to counter clock-wise
#def printCardsRound(round):
#    switcher = {
#       0: "",
#        1: "",
#        2: "",
#        3: "",
#        4: "",
#    }
#
#    print switcher.get(round, "No such round")

# printHands prints all possible poker hands in decesending order of probability 
def printHands():
    hands = HANDS()
    for x in hands:
        print(str(hands.index(x))+":"+x)

# printHandOdds prints the probabilities for each poker odds in decesending order 
#def printHandOdds():
#    print(list(HANDS_ODDS()))

# printHandProbabilities prints the probabilities for each poker hand in decesending order 
def printHandProbabilities():
    probabilities = HAND_PROBABILITIES() 
    for x in probabilities:
        print(
