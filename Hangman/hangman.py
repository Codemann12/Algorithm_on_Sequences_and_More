import random

allWords = [
    "assassin",
    "bannerol",
    "birthday",
    "calamity",
    "charters",
    "cordials",
    "downtown",
    "eighteen",
    "feelgood",
    "firebugs" 
]

userName = input("Please Enter your name: ")
wordToGuess = random.choice(allWords)
blindWord = "********"
nbrOfRound = 0
succesfullGuess = 0

def allPositionOfChar(char):
    global succesfullGuess
    positions = {}
    for index, charx in enumerate(wordToGuess):
        if char == charx:
            positions[index] = char
    succesfullGuess += len(positions)
    return positions 


def setChar(char):
    global blindWord
    charList = list(blindWord)
    positions = allPositionOfChar(char)
    for key, value in positions.items():
        charList[key] = value
    blindWord = ''.join(charList)
    print(blindWord)


while(nbrOfRound != 8):
    if succesfullGuess == 8:
        print(userName+ " win with a score of: "+str(8-nbrOfRound))
        break
    inChar = input("Enter a character: ")
    if inChar not in wordToGuess:
        nbrOfRound += 1
        print(blindWord)
    else:
        setChar(inChar)
        nbrOfRound += 1

if succesfullGuess != 8:
    print(userName+" ...looser with a score of: "+ str(8-nbrOfRound))
