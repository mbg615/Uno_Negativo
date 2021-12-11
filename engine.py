import engine_functions
from random import randint, shuffle
from time import sleep


def main():
    # Create player list
    player_select = int(input("How many players do you have? "))
    if player_select == 0:
        exit(0)

    player_list = engine_functions.Player.player_list(player_select)

    # Create card deck
    card_deck = engine_functions.Deck.make_deck()

    # Give each player 7 cards
    player_cards = engine_functions.Player.deal_cards(player_list, card_deck)

    # Game Setup
    engine_functions.General.clear()
    initial_card = card_deck[randint(0, len(card_deck))]
    print("The starting card is:", engine_functions.General.color_cards(initial_card))
    store_card = initial_card
    cNumber, cColor, cType = engine_functions.General.card_parser(initial_card)

    # Start the game loop
    gameRunning = True
    while gameRunning:
        currentPlayer = player_list[0]
        print(player_list[0] + "'s turn:")
        print(player_cards[player_list[0]])

        # Evaluate if card is valid
        evaluating_card_type = True
        while evaluating_card_type:
            play_card = str(input("Type the card you want to play or type 'Draw Card' to draw from the deck: "))
            if play_card != "Draw Card" or "exit":
                store_card = play_card
            tNumber, tColor, tType = engine_functions.General.card_parser(play_card)

            if play_card == "exit":
                exit()

            if play_card == "Draw Card":
                drawn_card = engine_functions.Deck.draw_card(card_deck)
                print("You drew a", engine_functions.General.color_cards(drawn_card))
                
                tNumber, tColor, tType = engine_functions.General.card_parser(drawn_card)

                if tNumber == cNumber or tColor == cColor:
                    evaluating_selection = True
                    while evaluating_selection:
                        play_drawn = input("Do you want to play the card? (Yes or No) ")
                        if play_drawn == "Yes":
                            store_card = drawn_card
                            cNumber, cColor, cType = engine_functions.General.card_parser(drawn_card)
                            engine_functions.General.clear()
                            print("Card to play from:", engine_functions.General.color_cards(drawn_card))
                            evaluating_selection = False
                            evaluating_card_type = False
                        if play_drawn == "No":
                            evaluating_selection = False
                            evaluating_card_type = False
                        if play_drawn == "exit":
                            exit(0)
                        else:
                            print("Sorry, that is not an option")
                    #play_drawn = None
                else:
                    player_cards[player_list[0]].append(drawn_card)
                    sleep(2)
                    engine_functions.General.clear()
                    print("Card to play from:", store_card)
                    evaluating_card_type = False
                play_drawn = None
            else:
                if play_card in player_cards[player_list[0]]:
                    if tNumber == cNumber or tColor == cColor:  # Check to make sure that play card is in the players cards
                        evaluating_card_type = False
                        cont_flag = True
                    else:
                        print("Sorry that card cannot be played. Pick again!")
                        cont_flag = False

                    if tType != None and cType != None:
                        if tType == cType:
                            evaluating_card_type = False
                            cont_flag = True
                        else:
                            print("Sorry that card cannot be played. Pick again!")
                            cont_flag = False
                    if cont_flag == True:
                        # Remove the used card from the players hand
                        card_played = player_cards[player_list[0]].index(play_card)
                        player_cards[player_list[0]].pop(card_played)

                        next_card = play_card
                        cNumber, cColor, cType = engine_functions.General.card_parser(next_card)

                        engine_functions.General.clear()

                        print("Card to play from:", engine_functions.General.color_cards(next_card))
                        cont_flag = None

                else: 
                    print("Sorry you do not have that card in your hand. Pick again!")

                if not player_cards[player_list[0]]:
                    print("Congrats", player_list[0], "You won!")
                    exit()

        player_list = engine_functions.Player.player_cycle(player_list)

    exit()


if __name__ == "__main__":
    main()