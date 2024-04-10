from Pawn.Pawn import Pawn

########################################
#                                      #
#              Assassin                #
#                                      #
########################################

class Assassin(Pawn):
    initial_positions = {
        'red': (1, 0),
        'yellow': (1, 8),
        'blue': (7, 8),
        'green': (7, 0)
    }

    def __init__(self, color):
        super().__init__(color, Assassin.initial_positions[color], 'Assassin')

    def move(self, new_position, teams=None):
        """Move Assassin and possibly kill other pawn."""
        # Find pawn on the new position
        enemy_pawn = self.find_enemy_pawn(new_position, teams)
        if enemy_pawn:
            self.kill(enemy_pawn)

        # Move the Assassin
        super().move(new_position)

    def find_enemy_pawn(self, position, teams):
        """Find ennemy pawn on position."""
        for team in teams:
            for pawn in team:
                if pawn.position == position and pawn.is_alive and pawn.color != self.color:
                    return pawn
        return None

    def kill(self, target_pawn):
        """Kill ennemy pawn."""
        target_pawn.position = self.position
        target_pawn.set_alive(False)
