# Makes one standard Uno Deck from the cards.txt file
def makeDeck():
    cardFile = open("data/cards.txt","r")
    rawRead = cardFile.readlines()

    # Strip newline (\n)
    cardPool = []
    for element in rawRead:
        cardPool.append(element.strip())
    return cardPool

# Draw a card from a finite deck; The deck will refill its self if empty.
def drawCardFinite(deck):
    from random import randrange
    randNum = randrange(len(deck))
    card = deck[randNum]
    deck = deck.pop(randNum)
    if len(deck) == 0:
        deck = makeDeck()
    return card, deck

def drawCardInfinite(deck):
    from random import randrange
    randNum = randrange(len(deck))
    card = deck[randNum]
    return card