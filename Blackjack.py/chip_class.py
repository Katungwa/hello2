class Chips:
	def __init__(self,tot_chips):
		self.tot_chips = tot_chips
		self.bet = 0

	def gain_chips(self):
		self.tot_chips += self.bet

	def lose_chips(self):
		self.tot_chips -= self.bet


		