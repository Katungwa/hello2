#---------------Func takes in the amount of chips the player wants to bet----------------
def take_bet(chips):
	while True:
		try:
			chips.bet = int(input('How much are you willing to stake'))
		except ValueError:
			print("Don't be dumb, I except you to give me an integer")
		else:
			if chips.bet > chips.tot_chips :
				print('You cant exceed your total chips')
			else:
				break

#------------------- Funcs that give a player the option of adding more cards on their list--------------
def hit(deck,hand):
	hand.add_card(deck.remove_one())
	hand.adjust_ace()

def hit_or_stand(deck,hand):
	while True:
		choice = input("Do you want to hit or stand: h or s")
		if choice.lower() == 'h':
			hit(deck,hand)
		elif choice.lower() == 's':
			print("Its the dealers turn")
		else:
			print("Please take a look at the choices again")
			continue
		break

#-------------------Function Scenarios of wins and loses-------------------------
def player_win(chips):
	print('Katungwa Wins with a higher sum')
	return chips.gain_chips()
def dealer_win(chips):
	print("Katungwa Loses and Dealer wins")
	return chips.lose_chips()
def player_bust(chips):
	print("Katungwa Loses. He has exceeded the required amount")
	return chips.lose_chips()
def dealer_bust(chips):
	print("Dealer Loses. He has exceeded the required amount")
	return chips.gain_chips()
def draw():
	print("Its a Draww!!")

#--------------------Funcs for Displaying the contents of a player-------------------
def show_some(player_hand,dealer_hand):
	print("Dealers cards: \n < hidden card >")
	print(dealer_hand.at_hand[-1])
	print('Katungwa cards: ', *player_hand.at_hand, sep = '\n')

def show_all(player_hand,dealer_hand):
	print("Dealer cards:", *dealer_hand.at_hand, sep = '\n')
	print(f"Dealer cards sum is {dealer_hand.summ}")
	print('Katungwa cards:', *player_hand.at_hand, sep = '\n')
	print(f"Katungwa's cards sum is{player_hand.summ}")

