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

    def die(self, killer_color, teams):
        self.set_alive(False)

        self.transfer_team_to_killer(killer_color, teams)

    def transfer_team_to_killer(self, killer_color, teams):
        pass
        """
        for team in teams:
            for pawn in team:
                if pawn.color == self.color:
                    pawn.color = killer_color
                    pawn.image = pawn.get_image_path(killer_color, pawn.type, pawn.is_alive)
        """
