class Deck:
    # Makes one standard Uno Deck from the cards.txt file
    def makeDeck():
        cardFile = open("data/cards.txt", "r")
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

    # Draw infinite cards (Does not respect a typical deck)
    def drawCardInfinite(deck):
        from random import randrange
        randNum = randrange(len(deck))
        card = deck[randNum]
        return card


class Player:
    # Create the list of player's order
    def playerList(numOfPlayers):
        playerOrder = []
        playerOrder.extend(range(0, numOfPlayers))
        for element in playerOrder:
            playerOrder[element] = "Player " + str(element)
        return playerOrder

    # Cycles the player list by one value
    def playerCycle(playerList):
        storeVal = playerList[0]
        playerList.pop(0)
        playerList.append(storeVal)
        return playerList

    # Give the player a list of 7 starting cards
    def dealCards(playerList, deck):
        from random import randint, sample
        cards = sample(deck, 7)
        playerCards = dict.fromkeys(playerList, [cards])
        return playerCards


class General:
    def cardParser(cardName):
        # IMPORTANT - This parser relies on the standard naming scheme present
        # in the cards.txt file. If card names were changed, the parser will
        # have to be manually updated.

        cardName = str(cardName)

        # Empty card flags
        numFlag, colorFlag, typeFlag = None, None, None

        # Find the number of card
        from re import findall
        findNum = findall('[0-9]', str(cardName))

        if findNum:
            if findNum[0]:
                numFlag = findNum[0]

        # Find color type of card
        if "Red" in cardName:
            colorFlag = "red"
        elif "Yellow" in cardName:
            colorFlag = "yellow"
        elif "Green" in cardName:
            colorFlag = "green"
        elif "Blue" in cardName:
            colorFlag = "blue"

        # Find the type of Card
        if "Wild" in cardName:
            typeFlag = "wild"
        elif "Draw" in cardName:
            if "Two" in cardName:
                typeFlag = "draw2"
            elif "Four" in cardName:
                typeFlag = "draw4"
        elif "Skip" in cardName:
            typeFlag = "skip"
        elif "Reverse" in cardName:
            typeFlag = "reverse"

        return numFlag, colorFlag, typeFlag
