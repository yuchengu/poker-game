import random
from collections import defaultdict, Counter

class Deck():
	'''
	Representation of the card
	'''
	def __init__(self):
		self.value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
		self.suite = ['C', 'D', 'H', 'S']

	def create_deck(self):
		'''
		Get the deck
		'''
		deck = []
		for value in self.value:
			for suite in self.suite:
				deck.append((value, suite))
		return deck

test_card = Deck()
deck = test_card.create_deck()


class Hand():
	'''
	Representation of each player's hands
	'''
	def __init__(self, hand):
		self.deck = Deck().create_deck()
		self.hand = hand
		self.rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
					 '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
		self.sorted = []
		for card in self.hand:
			self.sorted.append(self.rank[card[0]])
		self.sorted.sort()

		self.value_dict = defaultdict(int)
		for card in self.sorted:
			self.value_dict[card] += 1
		# print(self.value_dict)
		self.suite_dict = defaultdict(int)
		for card in self.hand:
			self.suite_dict[card[1]] += 1
		# print(self.suite_dict)


	def is_royal_flush(self):
		if self.is_straight_flush() and self.sorted[-1] == 14:
			return True
		else:
			return False

	def is_straight_flush(self):
		if self.is_straight() and self.is_flush():
			return True
		else:
			return False

	def is_four_kind(self):
		if len(self.value_dict) == 2 and 4 in self.value_dict.values():
			return True
		else:
			return False

	def is_full_house(self):
		if len(self.value_dict) == 2 and 3 in self.value_dict.values():
			return True
		else:
			return False

	def is_flush(self):
		if len(self.value_dict) == 5 and \
				(self.sorted[-1] - self.sorted[0] == 4):
			return True
		else:
			return False

	def is_straight(self):
		if len(self.suite_dict) == 1:
			return True
		else:
			return False

	def is_three_kind(self):
		if len(self.value_dict) == 3 and 3 in self.value_dict.values():
			return True
		else:
			return False

	def is_two_pair(self):
		if len(self.value_dict) == 3 and 2 in self.value_dict.values():
			return True
		else:
			return False

	def is_pair(self):
		if len(self.value_dict) == 4 and 2 in self.value_dict.values():
			return True
		else:
			return False

	def is_high_card(self):
		if len(self.value_dict) == 5:
			return True
		else:
			return False

	def score(self):
		if self.is_high_card():
			return 1
		elif self.is_pair():
			return 2
		elif self.is_two_pair():
			return 3
		elif self.is_three_kind():
			return 4
		elif self.is_straight():
			return 5
		elif self.is_flush():
			return 6
		elif self.is_full_house():
			return 7
		elif self.is_four_kind():
			return 8
		elif self.is_straight_flush():
			return 9
		elif self.is_royal_flush():
			return 10

	def hand_name(self):
		if self.is_high_card():
			return 'has nothing special'
		elif self.is_pair():
			return 'has a pair'
		elif self.is_two_pair():
			return 'has two pairs'
		elif self.is_three_kind():
			return 'is three of a kind'
		elif self.is_straight():
			return 'is a straight'
		elif self.is_flush():
			return 'is a flush'
		elif self.is_full_house():
			return 'is full house'
		elif self.is_four_kind():
			return 'is four of a kind'
		elif self.is_straight_flush():
			return 'is a straight flush'
		elif self.is_royal_flush():
			return 'is a royal flush'

	def checker(self):
		if self.is_high_card() or self.is_straight() or self.is_flush() or self.is_straight_flush():
			return self.sorted[-1]
		else:
			helper = []
			for key in self.value_dict:
				if self.is_pair():
					if self.value_dict[key] == 2:
						return key
				elif self.is_two_pair():
					if self.value_dict[key] == 2:
						helper.append(key)
						return max(helper)
				elif self.is_three_kind() or self.is_full_house():
					if self.value_dict[key] == 3:
						return key
					if self.value_dict[key] == 2:
						helper.append(key)
						return helper
				elif self.is_four_kind():
					if self.value_dict[key] == 4:
						return key


# # Test Cases
# test_flush = Hand([('9','D'),('10', 'H'),('J', 'H'),('Q', 'S'), ('K', 'D')])
# print(test_flush.is_flush())

# test_straight = Hand([('9','H'),('10', 'H'),('10', 'H'),('Q', 'H'), ('K', 'H')])
# print(test_straight.is_straight())

# test_straight_flush = Hand([('9','H'),('10', 'H'),('J', 'H'),('Q', 'H'), ('K', 'H')])
# print(test_straight_flush.is_straight_flush())

# test_royal_flush = Hand([('10', 'H'),('J', 'H'),('Q', 'H'), ('K', 'H'), ('A','H')])
# print(test_royal_flush.is_royal_flush())

# test_four = Hand([('10','D'),('10', 'H'),('10', 'H'),('10', 'S'), ('K', 'D')])
# print(test_four.is_four_kind())

# test_full = Hand([('10','D'),('10', 'H'),('10', 'H'),('K', 'S'), ('K', 'D')])
# print(test_full.is_full_house())

# test_three = Hand([('10','D'),('10', 'H'),('10', 'H'),('K', 'S'), ('J', 'D')])
# print(test_three.is_three_kind())

# test_two = Hand([('10','D'),('10', 'H'),('K', 'H'),('K', 'S'), ('J', 'D')])
# print(test_two.is_two_pair())

# test_one = Hand([('10','D'),('10', 'H'),('K', 'H'),('Q', 'S'), ('J', 'D')])
# print(test_one.is_pair())
# print(test_one.score())

# test_one = Hand([('7','D'),('10', 'H'),('K', 'H'),('Q', 'S'), ('J', 'D')])
# print(test_one.is_pair())

# print(test.get_card_value('A'))

class Deal():
	def __init__(self, number_of_players):
		self.number_of_players = number_of_players
		self.name = [input("Enter the names of the player: ") for i in range(number_of_players)]
		self.deck = Deck().create_deck()

	def one_deal(self):
		'''
		Remove the dealed cards from the deck after each deal
		'''
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

# test = Deal(3)
# test.deal()

class Game():
	def __init__(self, number_of_players):
		self.number_of_players = number_of_players
		self.match = Deal(self.number_of_players).deal()
		self.play = {}
		self.check = {}
		self.type = {}
		for player, hand in self.match.items():
			self.store = Hand(hand)
			# Get the mapping of the players with the checker
			self.check[player] = self.store.checker()
			# Get the mapping of the players with the score
			self.play[player] = self.store.score()
			# Get the mapping of the players with the type of hands
			self.type[player] = self.store.hand_name()
		# print(self.play)
		# print(self.match)
	def play_game(self):
		max_s = max(self.play.values())
		max_p = []
		for player, score in self.play.items():
			if score == max_s:
				max_p.append(player)
		if len(max_p) == 1:
			winner = max_p[0]
			print("The winner is {} with the hand of {}, which {}."\
						.format(winner, self.match[winner], self.type[winner]))

		else:
			for key, value in self.play.items():
				if key not in max_p:
					self.check[key] = 0
			new_max = max(self.check.values())
			for players in self.check.keys():
				if self.check[players] == new_max:
					new_winner = players
					print("The winner is {} with the hand of {}, which {}."\
						.format(new_winner, self.match[new_winner], self.type[new_winner]))
			return None


game_test = Game(4)
game_test.play_game()


