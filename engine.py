import engine_functions
from random import randint, shuffle
from time import sleep


def main():
    # Print game information:
    engine_functions.General.clear()
    print("Game Version: v0.9.2 pre-Alpha")

    # Create player list
    player_select = int(input("How many players do you have? "))

    if player_select <= 0:
        exit(0)

    player_list = engine_functions.Player.player_list(player_select)

    # Create card deck
    card_deck = engine_functions.Deck.make_deck()

    # Give each player 7 cards
    player_cards = engine_functions.Player.deal_cards(player_list, card_deck)

    # Game Setup
    engine_functions.General.clear()
    initial_card = card_deck[randint(0, len(card_deck))]
    while initial_card == "Draw Four": # Protect against use as a starting card
        initial_card = card_deck[randint(0, len(card_deck))]
    if initial_card == "Wild": # Allow first player to choose the card starting color
        pass
    print("The starting card is:", engine_functions.General.color_cards(initial_card))
    store_card = play_card = next_card = initial_card
    cNumber, cColor, cType = engine_functions.General.card_parser(initial_card)

    # Start the game loop
    gameRunning = True
    while gameRunning:
        if draw_two_flag == True:
            print("You drew 2 cards")
            player_list = engine_functions.Player.player_cycle(player_list)

        elif draw_four_flag == True:
            print("You drew 4 cards")
            player_list = engine_functions.Player.player_cycle(player_list)

        currentPlayer = player_list[0]
        print(currentPlayer + "'s turn:" + "\n", player_cards[currentPlayer])

        if play_card != "Draw Card":
            store_card = play_card

        # Evaluate if card is valid
        evaluating_card_type = True
        while evaluating_card_type:
            play_card = str(input("Type the card you want to play or type 'Draw Card' to draw from the deck: "))

            if play_card == "exit":
                exit()

            tNumber, tColor, tType = engine_functions.General.card_parser(play_card)

            if play_card == "Draw Card": # If the player wants to draw a card
                drawn_card = engine_functions.Deck.draw_card(card_deck)
                print("You drew a", engine_functions.General.color_cards(drawn_card))
                
                tNumber, tColor, tType = engine_functions.General.card_parser(drawn_card)

                if engine_functions.General.updated_card_verify(play_card, play_card):
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

                        elif play_drawn == "No":
                            evaluating_selection = False
                            evaluating_card_type = False

                        elif play_drawn == "exit":
                            exit(0)

                        else:
                            print("Sorry, that is not an option")

                # The player drew a card they cannot play
                else:
                    player_cards[player_list[0]].append(drawn_card)
                    sleep(2)
                    engine_functions.General.clear()
                    print("Card to play from:", engine_functions.General.color_cards(store_card))
                    evaluating_card_type = False
                play_drawn = None

            elif "Skip" in play_card: # If a player plays a Skip card
                if play_card in player_cards[player_list[0]]:
                    if engine_functions.General.updated_card_verify(play_card, play_card):
                        # Remove the card from the players card
                        card_played = player_cards[player_list[0]].index(play_card)
                        player_cards[player_list[0]].pop(card_played)

                        next_card = play_card
                        cNumber, cColor, cType = engine_functions.General.card_parser(next_card)

                        engine_functions.General.clear()

                        print("Card to play from:", engine_functions.General.color_cards(next_card))
                        player_list = engine_functions.Player.skip_player(player_list)

                        evaluating_card_type = False

                    else:
                        print("Sorry that card cannot be played. Pick again!")

                else: 
                    print("Sorry you do not have that card in your hand. Pick again!")

            elif "Reverse" in play_card:
                if play_card in player_cards[player_list[0]]:
                    if engine_functions.General.updated_card_verify(play_card, play_card):
                        # Remove the card from the players card
                        card_played = player_cards[player_list[0]].index(play_card)
                        player_cards[player_list[0]].pop(card_played)

                        next_card = play_card
                        cNumber, cColor, cType = engine_functions.General.card_parser(next_card)

                        engine_functions.General.clear()

                        print("Card to play from:", engine_functions.General.color_cards(next_card))
                        player_list = engine_functions.Player.reverse_order(player_list)

                        evaluating_card_type = False

                    else:
                        print("Sorry that card cannot be played. Pick again!")

                else: 
                    print("Sorry you do not have that card in your hand. Pick again!")
            
            elif "Draw Two" in play_card:
                if play_card in player_cards[player_list[0]]:
                    if engine_functions.General.updated_card_verify(play_card, play_card):
                        # Remove the card from the players hand
                        card_played = player_cards[player_list[0]].index(play_card)
                        player_cards[player_list[0]].pop(card_played)

                        next_card = play_card
                        cNumber, cColor, cType = engine_functions.General.card_parser(next_card)

                        print("Card to play from:", engine_functions.General.color_cards(next_card))

                        player_cards[player_list[1]].extend(engine_functions.Deck.draw_multiple_cards(card_deck, 2))

                        evaluating_card_type = False
                        draw_two_flag = True

                    else:
                        print("Sorry that card cannot be played. Pick again!")

                else:
                     print("Sorry you do not have that card in your hand. Pick again!")
            
            elif play_card == "Draw Four": # If the player plays a Draw Four
                if play_card in player_cards[player_list[0]]:
                    # Remove the card from the players hand
                        card_played = player_cards[player_list[0]].index(play_card)
                        player_cards[player_list[0]].pop(card_played)

                        next_card = play_card
                        cNumber = cType = "Any"
                        cColor = str(input("What color do you choose? (Red, Yellow, Green, Blue): "))

                        engine_functions.General.clear()
                        print("Card to play from:", engine_functions.General.color_cards(cColor + " " + next_card))

                        player_cards[player_list[1]].extend(engine_functions.Deck.draw_multiple_cards(card_deck, 4))

                        evaluating_card_type = False
                        draw_four_flag = True

                else:
                    print("Sorry you do not have that card in your hand. Pick again!")
            
            elif play_card == "Wild":
                pass

            else: # If the player plays a number card
                store_card = play_card
                if play_card in player_cards[player_list[0]]:
                    if engine_functions.General.updated_card_verify(play_card, play_card):
                        # Remove the used card from the players hand
                        card_played = player_cards[player_list[0]].index(play_card)
                        player_cards[player_list[0]].pop(card_played)

                        next_card = play_card
                        cNumber, cColor, cType = engine_functions.General.card_parser(next_card)

                        engine_functions.General.clear()

                        print("Card to play from:", engine_functions.General.color_cards(next_card))
                        evaluating_card_type = False

                    else:
                        print("Sorry that card cannot be played. Pick again!")

                else: 
                    print("Sorry you do not have that card in your hand. Pick again!")

        if not player_cards[player_list[0]]: # Stops the game if the players hand is empty
            print("Congrats", player_list[0], "You won!")
            exit()

        player_list = engine_functions.Player.player_cycle(player_list)

    exit()


if __name__ == "__main__":
    main()