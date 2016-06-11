import sys
import csv

class Player:
    VERSION = "rank data"
    HIGH = ['T', 'J', 'Q', 'K', 'A']
    CARD_VALUE = {'T': 10, 'J': 11, 'Q' :12 , 'K' :13, 'A': 14, '2': 2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8': 8, '9': 9, '10':10}
    MEDIUM = ['7', '8', '9']
    MAX_CHIPS = 3000

    #parses the json hand into a string in order to match with the probabilities csv file.
    def getHandString(self, monty_hole_cards):
        pair = self.isPair(monty_hole_cards)

        if pair:
            return '{0}{0}'.format(pair)

        cards = [card['rank'] for card in monty_hole_cards]

        if int(self.CARD_VALUE[cards[0]]) < int(self.CARD_VALUE[cards[1]]):
            cards.reverse()

        if len(cards) == 2:
            if self.isSuited(monty_hole_cards):
                return '{0}{1}s'.format(cards[0],cards[1])
            else:
                return '{0}{1}o'.format(cards[0],cards[1])

        print >> sys.stderr, 'This should not happen.'
        return "72o"

    # determines if the hand is suited
    def isSuited(self, monty_hole_cards):
        cards = [card['suit'] for card in monty_hole_cards]
        if len(cards) == 2:
            if cards[0] == cards[1]:
                return True
            else:
                return False

    #isPair returns the pair rank if the cards are pair, it returns false otherwise
    def isPair(self, monty_hole_cards):
        cards = [card['rank'] for card in monty_hole_cards]
        if len(cards) == 2:
            if cards[0] == cards[1]:
                return cards[0]
            else:
                return None

    #Suited connectors are two consecutive cards of the same suit
    #isSuitedConnector should return the (HIGH card, suit) of the connector if True, False otherwise
    def isSuitedConnector(self, monty_hole_cards):
        pass

    def betRequest(self, game_state):
        PREFLOP_PROBABILITIES = self.get_probability_dict('preflop_probabilities.csv')
        monty_index = game_state['in_action']
        monty = game_state['players'][monty_index]
        monty_hole_cards = monty['hole_cards']

        hand_string = self.getHandString(monty_hole_cards)
        probability = PREFLOP_PROBABILITIES[hand_string]
        # big_blind = 2 * game_state['small_blind']
        if probability > .33:
            bet = probability / .65 * monty['stack']
        else:
            bet = 4.0 * game_state['small_blind']
        return int(bet)

        # if self.isPair(monty_hole_cards):
        #     if self.isPair(monty_hole_cards) in self.HIGH:
        #         return self.MAX_CHIPS

        # max_bet = 0
        # for card in monty_hole_cards:
        #     rank = card['rank']
        #     if rank in self.HIGH:
        #         max_bet += 700
        #     elif rank in self.MEDIUM:
        #         max_bet += 300
        #     else:
        #         max_bet += 50

        # return max_bet

    def showdown(self, game_state):
        print >> sys.stderr, 'Showdown!'
        print >> sys.stderr, str( game_state['game_id'] )
        return 0

    def get_probability_dict(self, csv_file):
        with open(csv_file, mode='r') as infile:
            reader = csv.reader(infile, delimiter='\t')
            dict = {rows[0]:float(rows[1]) for rows in reader}
            return dict

