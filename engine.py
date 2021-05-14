import engineFunctions
from random import randint, shuffle
from time import sleep


def main():
    # Create player list
    playerSelect = int(input("How many players do you have? "))
    playerList = engineFunctions.Player.playerList(playerSelect)

    # Create card deck
    cardDeck = engineFunctions.Deck.makeDeck()

    # Give each player 7 cards
    playerCards = engineFunctions.Player.dealCards(playerList, cardDeck)

    # Game Setup
    engineFunctions.General.clear()
    initialCard = cardDeck[randint(0, len(cardDeck))]
    print("The starting card is:", initialCard)
    storeCard = initialCard
    cNumber, cColor, cType = engineFunctions.General.cardParser(initialCard)

    # Start the game loop
    gameRunning = True
    while gameRunning:
        currentPlayer = playerList[0]
        print(playerList[0] + "'s turn:")
        print(playerCards[playerList[0]])

        # Evaluate if card is valid
        evaluatingCardType = True
        while evaluatingCardType:
            playCard = str(input("Type the card you want to play or type 'Draw Card' to draw from the deck: "))
            if playCard != "Draw Card":
                storeCard = playCard
            tNumber, tColor, tType = engineFunctions.General.cardParser(playCard)

            if playCard == "Draw Card":
                drawnCard = engineFunctions.Deck.drawCard(cardDeck)
                print("You drew a", drawnCard)
                
                tNumber, tColor, tType = engineFunctions.General.cardParser(drawnCard)

                if tNumber == cNumber or tColor == cColor:
                    playDrawn = input("Do you want to play the card? (Yes or No) ")
                    if playDrawn == "Yes":
                        storeCard = drawnCard
                        nextCard = drawnCard
                        cNumber, cColor, cType = engineFunctions.General.cardParser(nextCard)
                        engineFunctions.General.clear()
                        print("Card to play from:", nextCard)
                        evaluatingCardType = False
                    if playDrawn == "No":
                        evaluatingCardType = False
                    playDrawn = None
                else:
                    playerCards[playerList[0]].append(drawnCard)
                    sleep(2)
                    engineFunctions.General.clear()
                    print("Card to play from:", storeCard)
                    evaluatingCardType = False
                playDrawn = None
            else:
                if playCard in playerCards[playerList[0]]:
                    if tNumber == cNumber or tColor == cColor:  # Check to make sure that play card is in the players cards
                        evaluatingCardType = False
                        contFlag = True
                    else:
                        print("Sorry that card cannot be played. Pick again!")
                        contFlag = False

                    if tType != None and cType != None:
                        if tType == cType:
                            evaluatingCardType = False
                            contFlag = True
                        else:
                            print("Sorry that card cannot be played. Pick again!")
                            contFlag = False
                    if contFlag == True:
                        # Remove the used card from the players hand
                        cardToPop = playerCards[playerList[0]].index(playCard)
                        playerCards[playerList[0]].pop(cardToPop)

                        nextCard = playCard
                        cNumber, cColor, cType = engineFunctions.General.cardParser(nextCard)

                        engineFunctions.General.clear()

                        print("Card to play from:", nextCard)
                        contFlag = None

                else:
                    print("Sorry you do not have that card in your hand. Pick again!")

                if not playerCards[playerList[0]]:
                    print("Congrats", playerList[0], "You won!")
                    exit()

        playerList = engineFunctions.Player.playerCycle(playerList)


if __name__ == "__main__":
    main()
