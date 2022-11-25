from deck_class import *
from hand_class import *
from variables import *
from chip_class import *
from functions import *

playing = True
keep_going = True
player_chips = Chips(2000)
while keep_going:
	print("The game has very simple game rules, Make sure that the sum of your cards does not exceed 21. \n The one whose player cards are nearest to 21 wins")
	my_deck = Deck()
	my_deck.shuffle_cards()

	players_hand = Hand(suits,ranks)
	players_hand.add_card(my_deck.remove_one())
	players_hand.add_card(my_deck.remove_one())

	dealers_hand = Hand(suits,ranks)
	dealers_hand.add_card(my_deck.remove_one())
	dealers_hand.add_card(my_deck.remove_one())

	show_some(players_hand,dealers_hand)

	player_chips = Chips(2000)
	take_bet(player_chips)

	while playing:
		hit_or_stand(my_deck,players_hand)
		
		if players_hand.summ > 21:
			player_bust(player_chips)
			show_all(players_hand,dealers_hand)	
		if players_hand.summ <= 21:
			while dealers_hand.summ < 17:
				hit(my_deck,dealers_hand)
			show_all(players_hand,dealers_hand)
			if players_hand.summ > dealers_hand.summ:
				player_win(player_chips)
			if players_hand.summ < dealers_hand.summ:
				dealer_win(player_chips)
			if dealers_hand.summ > 21:
				player_win(player_chips)
			else:
				draw()
		print(f'Katus remaining chips are {player_chips.tot_chips}')
		player_chips = player_chips.tot_chips

		playing = False
	keep_going = False
	game_on = input('Should we restart the game? y or n')
	if game_on.lower() == 'y':
		keep_going = True
		playing = True
	else:
		print('Game_over')



