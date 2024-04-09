import constantes


########################################
#                                      #
#            Global Pawn               #
#                                      #
########################################

class Pawn:
    def __init__(self, color, position, pawn_type):
        self.color = constantes.color[color.upper()]
        self.position = tuple(position)
        self.is_alive = True
        self.type = pawn_type
        self.image = self.get_image_path(color, pawn_type, self.is_alive)
        # Scale the image to fit the square size
        self.scale = (constantes.SQUARE_SIZE * 0.8, constantes.SQUARE_SIZE * 0.8)
        self.max_range = constantes.ROWS    

    def get_image_path(self, color, pawn_type, is_alive):
        # Make sure the color is a tuple
        if isinstance(color, str):
            color = constantes.color.get(color.upper(), (0, 0, 0))

        # Convert the color to a color name
        color_name = constantes.COLOR_NAMES.get(color, 'unknown')
        state_folder = "Alive" if is_alive else "Died"
        status = "" if is_alive else "_died"
        return f'./assets/{state_folder}/{pawn_type}_token_{color_name}{status}.png'

    def set_alive(self, alive):
        self.is_alive = alive
        # Update the image path based on the new state of the pawn (alive or dead)
        self.image = self.get_image_path(self.color, self.type, self.is_alive)

    def move(self, new_position, teams=None):
        self.position = tuple(new_position)

    def __can_move(self, new_position, teams):
        # Check if the new position is outside the board
        if not (0 <= new_position[0] < 9 and 0 <= new_position[1] < 9):
            return False
        # Check if the new position is the labyrinth position and the pawn is not a chief
        if new_position == constantes.LABYRINTH_POSITION and self.type != 'Chief':
            return False
        # Check if the new position is occupied by an ally
        for team in teams:
            for ally in team:
                if ally.color == self.color and ally.position == new_position and ally.is_alive:
                    return False

        return True

    def __get_possible_moves(self, teams, dx, dy):
        moves = []
        for i in range(1, self.max_range):  # Diag vers le bas dte
            new_position = (self.position[0] + dx*i, self.position[1] + dy*i)
            if self.__can_move(new_position, teams):
                moves.append(new_position)
                # Break if an enemy pawn is encountered
                if self.find_enemy_pawn(new_position, teams):
                    break
            else:
                break
        return moves

    def get_possible_moves(self, teams):
        possible_moves = []
        possible_moves.extend(self.__get_possible_moves(teams, 1, 1))
        possible_moves.extend(self.__get_possible_moves(teams, -1, -1))
        possible_moves.extend(self.__get_possible_moves(teams, -1, 1))
        possible_moves.extend(self.__get_possible_moves(teams, 1, -1))
        possible_moves.extend(self.__get_possible_moves(teams, 1, 0))
        possible_moves.extend(self.__get_possible_moves(teams, 0, 1))
        possible_moves.extend(self.__get_possible_moves(teams, 0, -1))
        possible_moves.extend(self.__get_possible_moves(teams, -1, 0))
        return possible_moves

    def find_enemy_pawn(self, position, teams):
        """Find ennemy pawn on select position."""
        for team in teams:
            for pawn in team:
                if pawn.position == position and pawn.is_alive and pawn.color != self.color:
                    return pawn
        return None

    def get_adjacent_position(self, direction):
        """Get adjacent position."""
        dx, dy = 0, 0
        if direction == "up":
            dy = -1
        elif direction == "down":
            dy = 1
        elif direction == "left":
            dx = -1
        elif direction == "right":
            dx = 1
        return self.position[0] + dy, self.position[1] + dx
    
    def __repr__(self):
        return self.__class__.__name__