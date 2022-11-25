from card_class import *
from deck_class import *
from variables import *
class Hand(Card):
	def __init__(self,suit,rank):
		super().__init__(suit,rank)
		self.at_hand = []
		self.summ = 0
		self.aces = 0

	def add_card(self,new_card):
		self.at_hand.append(new_card)
		self.summ +=  values[new_card.rank]
		if new_card.rank == 'ace':
			self.aces += 1

	def adjust_ace(self):
		while self.summ > 21 and self.aces:
			self.summ -= 10
			self.aces -= 1




