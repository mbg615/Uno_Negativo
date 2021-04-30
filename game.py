import gameFunctions

def main():
    # Create player order and card deck
    playerSelect = int(input("How many players do you have? "))
    deckType = int(input("Infinite deck (0) or realistic deck (1) "))
    cardDeck = gameFunctions.Deck.makeDeck()
    playerList = gameFunctions.Player.playerList(playerSelect)
    
    

if __name__ == "__main__":
    main()