from Pawn.Pawn import Pawn

########################################
#                                      #
#               Chief                  #
#                                      #
########################################

class Chief(Pawn):
    initial_positions = {
        'red': (0, 0),
        'yellow': (0, 8),
        'blue': (8, 8),
        'green': (8, 0)
    }

    def __init__(self, color):
        super().__init__(color, Chief.initial_positions[color], 'Chief')
