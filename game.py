import gameFunctions
from random import randint


def main():
    # Create player order and card deck
    playerSelect = int(input("How many players do you have? "))
    cardDeck = gameFunctions.Deck.makeDeck()
    playerList = gameFunctions.Player.playerList(playerSelect)

    playerCardStats = gameFunctions.Player.dealCards(playerList, cardDeck)

    initialCard = cardDeck[randint(0, len(cardDeck))]
    print("The play card is:", initialCard)
    cNumber, cColor, ctype = gameFunctions.General.cardParser(initialCard)
    print(cNumber, cColor, ctype)

    # Start the game loop
    gameRunning = True
    while gameRunning is True:
        pass


if __name__ == "__main__":
    main()
