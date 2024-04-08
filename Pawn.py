import random

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
        for i in range(1, constantes.ROWS):  # Diag vers le bas dte
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


########################################
#                                      #
#              Militant                #
#                                      #
########################################

class Militant(Pawn):
    initial_positions = {
        'red': [(2, 0), (2, 1), (0, 2), (1, 2)],
        'yellow': [(0, 6), (1, 6), (2, 7), (2, 8)],
        'blue': [(7, 6), (8, 6), (6, 7), (6, 8)],
        'green': [(6, 0), (6, 1), (7, 2), (8, 2)]
    }

    def __init__(self, color, index):
        initial_position = Militant.initial_positions[color][index]
        super().__init__(color, initial_position, 'Militant')

    def __can_move(self, new_position, teams):
        # Check if the new position is outside the board
        if not (0 <= new_position[0] < 9 and 0 <= new_position[1] < 9):
            return False
        # Check if the new position is the labyrinth position and the pawn is not a chief
        if new_position == constantes.LABYRINTH_POSITION and self.type != 'Chief':
            return False
        # Check if the new position is occupied by an ally
        for team in teams:
            for pawn in team:
                if pawn.position == new_position and pawn.color == self.color:
                    return False
        # Check if the new position is occupied by a chief
        for team in teams:
            for pawn in team:
                if pawn.position == new_position and pawn.type == 'Chief':
                    return False
        # Check if the new position is a valid move for the pawn
        dx = new_position[0] - self.position[0]
        dy = new_position[1] - self.position[1]
        return (dx == 0 or dy == 0 or abs(dx) == abs(dy)) and max(abs(dx), abs(dy)) <= 2

    def move(self, new_position, teams=None):
        enemy_pawn = self.find_enemy_pawn(new_position, teams)
        if enemy_pawn and enemy_pawn.type != 'Chief':
            self.kill(enemy_pawn, teams)
        super().move(new_position)

    def kill(self, target_pawn, teams):
        target_pawn.set_alive(False)
        free_positions = self.find_free_positions(teams)
        if free_positions:
            new_position_for_dead = random.choice(free_positions)
            target_pawn.position = new_position_for_dead

    def find_free_positions(self, teams):
        all_positions = [(x, y) for x in range(9) for y in range(9)]
        occupied_positions = [pawn.position for team in teams for pawn in team if pawn.is_alive]
        return [pos for pos in all_positions if pos not in occupied_positions]


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
