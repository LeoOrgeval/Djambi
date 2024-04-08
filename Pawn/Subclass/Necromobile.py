from Pawn.Pawn import Pawn

########################################
#                                      #
#            Necromobile               #
#                                      #
########################################

class Necromobile(Pawn):
    initial_positions = {
        'red': (2, 2),
        'yellow': (2, 6),
        'blue': (6, 6),
        'green': (6, 2)
    }

    def __init__(self, color):
        super().__init__(color, Necromobile.initial_positions[color], 'Necromobile')
