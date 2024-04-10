from Pawn.Pawn import Pawn

########################################
#                                      #
#              Diplomat                #
#                                      #
########################################


class Diplomat(Pawn):
    initial_positions = {
        'red': (0, 1),
        'yellow': (0, 0),
        'blue': (8, 7),
        'green': (8, 1)
    }

    def __init__(self, color):
        super().__init__(color, Diplomat.initial_positions[color], 'Diplomat')

    def move(self, new_position, teams=None):
        """Move Assassin and possibly move other pawn."""
        # Find pawn on the new position
        enemy_pawn = self.find_enemy_pawn(new_position, teams)
        if enemy_pawn:
            self.move_pawn(enemy_pawn)

        # Move the Assassin
        super().move(new_position)

    def find_enemy_pawn(self, position, teams):
        """Find ennemy pawn on position."""
        for team in teams:
            for pawn in team:
                if pawn.position == position and pawn.is_alive and pawn.color != self.color:
                    return pawn
        return None

    def __can_move(self, new_position, teams):
        # Check if the new position is outside the board
        if not (0 <= new_position[0] < 9 and 0 <= new_position[1] < 9):
            return False
        # Check if the new position is occupied by an ally
        for team in teams:
            for pawn in team:
                if pawn.position == new_position and pawn.color == self.color:
                    return False
        # Check if the new position is a valid move for the pawn
        dx = new_position[0] - self.position[0]
        dy = new_position[1] - self.position[1]
        return (dx == 0 or dy == 0 or abs(dx) == abs(dy)) and max(abs(dx), abs(dy)) <= 2

    def move_pawn(self, target_pawn):
        # Moving pawn
        target_pawn.position = self.position

    # def get_possible_moves(self, teams):
    #     possible_moves = []
    #     for dx in range(-10, 10):
    #         for dy in range(-10, 10):
    #             new_position = (self.position[0] + dx, self.position[1] + dy)
    #             if self.__can_move(new_position, teams):
    #                 possible_moves.append(new_position)
    #     return possible_moves