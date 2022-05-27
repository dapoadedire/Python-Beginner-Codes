import random

SUIT_TUPLE = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
RANK_TUPLE = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
NCARDS= 8

def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut
    

print('Welcome to Higher or Lower!')
print('You will be dealt a card and then asked if you think the next card will be higher or lower.')
print('Getting it right adds 20 points, getting it wrong you lose 10 points')
print('You have 50 points to start, get to 100 points to win the game.')
print('If you get to 0 points, you lose!')
print('Good Luck!')

print('\n')
print('\n')
print('\n')
startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit,
        'value':thisValue + 1}
        startingDeckList.append(cardDict)
score = 50
while True: # play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()