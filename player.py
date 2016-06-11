import sys

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        return 1000

    def showdown(self, game_state):
        print >> sys.stderr, 'Showdown!'
        print >> sys.stderr, str( game_state['game_id'] )
        return 0
