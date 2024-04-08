from Pawn.Pawn import Pawn
import constantes

########################################
#                                      #
#              Reporter                #
#                                      #
########################################

class Reporter(Pawn):
    initial_positions = {
        'red': (1, 1),
        'yellow': (1, 7),
        'blue': (7, 7),
        'green': (7, 1)
    }

    def __init__(self, color):
        super().__init__(color, Reporter.initial_positions[color], 'Reporter')

    def kill_adjacent_pawn(self, direction, teams):
        """
        Kills an adjacent pawn in the specified direction if possible.
        :param direction: The direction to kill ('up', 'down', 'left', 'right').
        :param teams: List of all teams (to find enemy pawns).
        """
        # Define movement based on direction
        directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }
        move_dx, move_dy = directions.get(direction, (0, 0))

        # Calculate the position of the adjacent pawn
        adjacent_x = self.position[0] + move_dx
        adjacent_y = self.position[1] + move_dy
        adjacent_position = (adjacent_x, adjacent_y)

        # Check if adjacent position is within the board
        if not (0 <= adjacent_x < constantes.ROWS and 0 <= adjacent_y < constantes.COLS):
            return

        # Find and kill the adjacent enemy pawn if present
        for team in teams:
            for pawn in team:
                if pawn.position == adjacent_position and pawn.is_alive and pawn.color != self.color:
                    pawn.set_alive(False)
                    # Mise à jour après l'élimination Vous pouvez ajouter ici du code pour mettre à jour l'affichage
                    # ou effectuer d'autres actions nécessaires
                    return

    def can_kill(self, position, teams):
        """Check if reporter can kill pawn in select position."""
        for team in teams:
            for pawn in team:
                if pawn.position == position and pawn.color != self.color and pawn.is_alive:
                    return True
        return False
