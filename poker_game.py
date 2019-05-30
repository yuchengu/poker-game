import random
import sys

class Hand():
    '''
    Representation of each player's hands
    '''
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.name = [input("Enter the name of the players: ") for i in range(self.number_of_players)]
        self.deck = list(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4)

    def one_deal(self):
        '''
        Remove the dealed cards from the deck after each deal
        '''
        if len(self.deck) >= 5:
            one_hand = random.sample(self.deck, 5)
            for card in one_hand:
                if card in self.deck:
                    self.deck.remove(card)
            return one_hand

    def deal(self):
        '''
        Deal the hands for all players and record the name and hand
        '''
        map = {}
        for player in self.name:
            map[player] = self.one_deal()
        return map

# test = Hand(3)
# print((test.name))
# print(test.deal())

class Game():
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.card = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.match = Hand(number_of_players).deal()

    def get_card_value(self, card):
        '''
        Get the card value for a single card
        '''
        value = {}
        for key in self.card:
                value[key] = self.card.index(key) + 2
        return value[card]

    def get_hand_value(self):
        '''
        Get the sorted value of a hand of cards mapped with the players
        '''
        value_dict = {}
        for player, hand in self.match.items():
            hand_value = []
            for item in hand:
                value = self.get_card_value(item)
                hand_value.append(value)
                hand_value.sort()
                value_dict[player] = hand_value
        return value_dict

    def win(self):
        '''
        Play the game and return who will win the game
        '''
        i = 4
        while i >= 0:
            max_store = {}
            mapping = dict(self.get_hand_value())
            players = self.number_of_players
            for player, values in dict(mapping).items():
                max_store[player] = values[i]
                max_v = max(max_store.values())
                if len(max_store) == players:
                    if list(max_store.values()).count(max_v) == 1:
                        for key in max_store:
                            if max_store[key] == max_v:
                                max_p = key
                                return ('The winner is {} with the hand of {}'.format(max_p, self.match[max_p]))
                    else:
                        for key2 in max_store:
                            if max_store[key2] != max_v:
                                max_store[key2] = None

            i -= 1

# game_test = Game(5)
# print(game_test.get_hand_value())
# print(game_test.win())

# # Uncomment the following if running in terminal:
# first_arg = int(sys.argv[1])
# if first_arg <= 10:
#     play = Game(first_arg)
#     print(play.win())
# else:
#     print('There can be at most 10 players')
