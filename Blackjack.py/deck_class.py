
from variables import *
from card_class import Card
import random

class Deck():
	def __init__(self):
		self.deck_cards = []
		for suit in suits:
			for rank in ranks:
				self.deck_cards.append(Card(suit,rank))


	def __str__(self):
		deck_comp= ''

		for card in self.deck_cards:
			deck_comp +='\n' + card.__str__()
			
		return deck_comp

	# shufflin appended cards in deck_cards
	def shuffle_cards(self):
		random.shuffle(self.deck_cards)

	# remove the first card in deck_cards
	def remove_one(self):
		return self.deck_cards.pop(0)



