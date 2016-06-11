import sys

class Player:
    VERSION = "rank data"
    HIGH = ['10', 'J', 'Q', 'K', 'A']
    MEDIUM = ['7', '8', '9']
    MAX_CHIPS = 3000

    #isPair returns the pair rank if the cards are pair, it returns false otherwise
    def isPair(self, monty_hole_cards):
        cards = [card['rank'] for card in monty_hole_cards]
        if len(cards) == 2:
            if cards[0] == cards[1]:
                return cards[0]
            else:
                return False

    #Suited connectors are two consecutive cards of the same suit
    #isSuitedConnector should return the (HIGH card, suit) of the connector if True, False otherwise
    def isSuitedConnector(self, monty_hole_cards):
        pass

    def betRequest(self, game_state):
        big_blind = 2.0*game_state["small_blind"]
    	monty_index = game_state['in_action']
    	monty = game_state['players'][monty_index]
    	monty_hole_cards = monty['hole_cards']

        if self.isPair(monty_hole_cards):
            if self.isPair(monty_hole_cards) in self.HIGH:
                return self.MAX_CHIPS

    	max_bet = 0
    	for card in monty_hole_cards:
    		rank = card['rank']
    		if rank in self.HIGH:
    			max_bet += 700
    		elif rank in self.MEDIUM:
    			max_bet += 300
    		else:
    			max_bet += 50

    	return max_bet

    def showdown(self, game_state):
        print >> sys.stderr, 'Showdown!'
        print >> sys.stderr, str( game_state['game_id'] )
        return 0

