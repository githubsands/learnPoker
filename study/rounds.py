import random 

def NAME_OF_ROUNDS():
    rounds = {
    0: "preflop", 
    1: "flop",
    2: "turn", 
    3: "river", 
    4: "showdown", 
     }
    return rounds

#TODO: 
def generateRoundQuestions():
    rounds = NAME_OF_ROUNDS()

    num = random.choice(list(rounds.keys()))
    #key = rounds.get(num)

    return "What is the name of the" + num + "round?"

def generateRoundAnswer(num): 
    rounds = NAME_OF_ROUNDS()

def  
