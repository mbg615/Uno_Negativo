from random import randbytes


class Deck:
    # Makes one standard Uno Deck from the cards.txt file
    def make_deck():
        card_file = open("data/number_cards.txt", "r")
        raw_read = card_file.readlines()

        # Strip newline (\n)
        card_pool = []
        for element in raw_read:
            card_pool.append(element.strip())
        return card_pool

    # Draw infinite cards (Does not respect a typical deck)
    def draw_card(deck):
        from random import randrange
        rand_num = randrange(len(deck))
        card = deck[rand_num]
        return card

    # Draw multiple cards from the deck
    def draw_multiple_cards(deck, number):
        from random import randrange
        drawn_cards = []

        for i in range(0, number):
            rand_num = randrange(len(deck))
            drawn_cards.append(deck[rand_num])

        return drawn_cards
    
    # Color the deck cards using ANSII escape codes
    def color_deck(deck):
        colored_deck = []
        for card in deck:
            card_number, card_color, card_type = General.card_parser(card)
            if card_color == "red":
                colored_text = str(u"\u001b[38;5;$1m Red\u001b[0m ")
            if card_color == "yellow":
                colored_text = str(u"\u001b[38;5;$3m Yellow\u001b[0m ")
            if card_color == "green":
                colored_text = str(u"\u001b[38;5;$2m Green\u001b[0m ")
            if card_color == "blue":
                colored_text = str(u"\u001b[38;5;$4m Blue\u001b[0m ")

            if card_type == None:
                colored_card_name = colored_text + card_number
            if card_number == None:
                colored_card = colored_text + card_type

            colored_deck.append(colored_card)

        return colored_deck


class Player:
    # Create the list of player's order
    def player_list(num_of_players):
        player_order = []
        player_order.extend(range(0, num_of_players))
        for element in player_order:
            player_order[element] = "Player " + str(element + 1)
        return player_order

    # Cycles the player list by one value
    def player_cycle(player_list):
        store_val = player_list[0]
        player_list.pop(0)
        player_list.append(store_val)
        return player_list

    # Give the player a list of 7 starting cards
    def deal_cards(player_list, deck):
        from random import sample
        player_cards = dict.fromkeys(player_list, None)
        for keys in player_cards:
            cards = sample(deck, 7)
            player_cards[keys] = cards
        return player_cards
    
    # Skip the next player in line
    def skip_player(player_list):
        for i in range(0,2):
            store_val = player_list[0]
            player_list.pop(0)
            player_list.append(store_val)
        return player_list
    
    def reverse_order(player_list):
        return player_list.reverse()


class General:
    def card_parser(card_name):
        # IMPORTANT  - This parser relies on the standard naming scheme present
        # in the cards.txt file. If card names were changed, the parser will
        # have to be manually updated. Any cards added to the file will also have
        # to be aded to the parser inorder for the engine to know how to use them.

        card_name = str(card_name)

        # Empty card flags
        num_flag, color_flag, type_flag = None, None, None

        # Find the number of card
        from re import findall
        find_num = findall('[0-9]', str(card_name))

        if find_num:
            if find_num[0]:
                num_flag = find_num[0]

        # Find color type of card
        if "Red" in card_name:
            color_flag = "red"
        elif "Yellow" in card_name:
            color_flag = "yellow"
        elif "Green" in card_name:
            color_flag = "green"
        elif "Blue" in card_name:
            color_flag = "blue"

        # Find the type of Card
        if "Wild" in card_name:
            type_flag = "wild"
        elif "Draw" in card_name:
            if "Two" in card_name:
                type_flag = "draw2"
            elif "Four" in card_name:
                type_flag = "draw4"
        elif "Skip" in card_name:
            type_flag = "skip"
        elif "Reverse" in card_name:
            type_flag = "reverse"

        return num_flag, color_flag, type_flag

    # Verifys that the card a player tries to play will work
    def card_verify(player_card, last_play_card):
        equivalence_verify = False
        number_equivalence_played, color_equivalence_played, type_equivalence_played = General.card_parser(last_play_card)
        number_equivalence_test, color_equivalence_test, type_equivalence_test = General.card_parser(player_card)
        
        if number_equivalence_played == number_equivalence_test:
            equivalence_verify = True
        elif color_equivalence_played == color_equivalence_test:
            equivalence_verify = True
        elif type_equivalence_played == type_equivalence_test:
            equivalence_verify = True

        return equivalence_verify


    def clear():
        from os import system, name
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    # Injector function to run in place of direct card calls.
    def color_cards(card_name):
        card_number, card_color, card_type = General.card_parser(card_name)

        try:
            if card_color == "red":
                colored_text = str(u"\u001b[38;5;$1m Red\u001b[0m ")
            if card_color == "yellow":
                colored_text = str(u"\u001b[38;5;$3m Yellow\u001b[0m ")
            if card_color == "green":
                colored_text = str(u"\u001b[38;5;$2m Green\u001b[0m ")
            if card_color == "blue":
                colored_text = str(u"\u001b[38;5;$4m Blue\u001b[0m ")

            if card_type == None:
                colored_card_name = colored_text + card_number
            if card_number == None:
                colored_card = colored_text + card_type
        except:
            print("An error has occured with the card colorer")
            return card_name

        return colored_card_name