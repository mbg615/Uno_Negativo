import gameFunctions
from random import randint, shuffle


def main():
    # Create player list
    playerSelect = int(input("How many players do you have? "))
    playerList = gameFunctions.Player.playerList(playerSelect)

    # Create card deck
    cardDeck = gameFunctions.Deck.makeDeck()

    # Give each player 7 cards
    playerCards = gameFunctions.Player.dealCards(playerList, cardDeck)

    # Game Setup
    gameFunctions.General.clear()
    initialCard = cardDeck[randint(0, len(cardDeck))]
    print("The starting card is:", initialCard)
    cNumber, cColor, cType = gameFunctions.General.cardParser(initialCard)

    # Start the game loop
    gameRunning = True
    while gameRunning:
        currentPlayer = playerList[0]
        print(playerList[0] + "'s turn:")
        print(playerCards[playerList[0]])

        # Evaluate if card is valid
        evaluatingCardType = True
        while evaluatingCardType:
            playCard = str(input("Card to play or type 'Draw Card' to draw from the deck: "))
            tNumber, tColor, tType = gameFunctions.General.cardParser(playCard)

            if playCard == "Draw Card":
                playerCards[playerList] = gameFunctions.Player.drawCards(playerCards[playerList], cardDeck)
            else:
                if playCard in playerCards[playerList[0]]:
                    if tNumber == cNumber or tColor == cColor:  # Check to make sure that play card is in the players cards
                        evaluatingCardType = False
                    else:
                        print("Sorry that card cannot be played. Pick again!")

                    if tType != None and cType != None:
                        if tType == cType:
                            evaluatingCardType = False
                        else:
                            print("Sorry that card cannot be played. Pick again!")
                    
                    cardToPop = playerCards[playerList[0]].index(playCard)
                    playerCards[playerList[0]].pop(cardToPop)

                    nextCard = playCard
                    cNumber, cColor, cType = gameFunctions.General.cardParser(nextCard)

                    gameFunctions.General.clear()

                    print("Card to play from:", nextCard)


                else:
                    print("Sorry you do not have that card in your hand. Pick again!")

                # Remove the used card from the players hand
                # cardToPop = playerCards[playerList[0]].index(playCard)
                # playerCards[playerList[0]] = playerCards[playerList[0]].pop(cardToPop)
                # playerCards[playerList[0]].pop(cardToPop)

                if not playerCards[playerList[0]]:
                    print("Congrats", playerList[0], "You won!")
                    exit()

        playerList = gameFunctions.Player.playerCycle(playerList)


if __name__ == "__main__":
    main()
