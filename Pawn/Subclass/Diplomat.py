from Pawn.Pawn import Pawn

########################################
#                                      #
#              Diplomat                #
#                                      #
########################################

class Diplomat(Pawn):
    initial_positions = {
        'red': (0, 1),
        'yellow': (0, 7),
        'blue': (8, 7),
        'green': (8, 1)
    }

    def __init__(self, color):
        super().__init__(color, Diplomat.initial_positions[color], 'Diplomat')

