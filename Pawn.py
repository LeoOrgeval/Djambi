import constantes


def get_image_path(color, pawn_type, is_alive):
    # Determine the folder to look for the image based on the pawn's state (alive or dead)
    state_folder = "Alive" if is_alive else "Died"
    status = "" if is_alive else "_died"
    return f'./assets/{state_folder}/{pawn_type}_token_{color}{status}.png'


class Pawn:
    def __init__(self, color, position, pawn_type):
        self.color = constantes.color[color.upper()]
        self.position = tuple(position)
        self.is_alive = True
        self.type = pawn_type
        self.image = get_image_path(color, pawn_type, self.is_alive)
        # Scale the image to fit the square size
        self.scale = (constantes.SQUARE_SIZE * 0.8, constantes.SQUARE_SIZE * 0.8)

    def set_alive(self, alive):
        self.is_alive = alive
        # Update the image path based on the new state of the pawn (alive or dead)
        self.image = get_image_path(self.color, self.type, self.is_alive)

    def move(self, new_position):
        self.position = tuple(new_position)

    def can_move(self, new_position):
        # Check if the new position is outside the board
        if not (0 <= new_position[0] < 9 and 0 <= new_position[1] < 9):
            return False
        # Check if the new position is a valid move for the pawn
        dx = new_position[0] - self.position[0]
        dy = new_position[1] - self.position[1]
        return dx == 0 or dy == 0 or abs(dx) == abs(dy)

    def get_possible_moves(self):
        possible_moves = []
        for dx in range(-constantes.ROWS, constantes.ROWS):
            for dy in range(-constantes.COLS, constantes.COLS):
                new_position = (self.position[0] + dx, self.position[1] + dy)
                if self.can_move(new_position):
                    possible_moves.append(new_position)
        return possible_moves


class Assassin(Pawn):
    initial_positions = {
        'red': (1, 0),
        'yellow': (1, 8),
        'blue': (7, 8),
        'green': (7, 0)
    }

    def __init__(self, color):
        super().__init__(color, Assassin.initial_positions[color], 'Assassin')


class Reporter(Pawn):
    initial_positions = {
        'red': (1, 1),
        'yellow': (1, 7),
        'blue': (7, 7),
        'green': (7, 1)
    }

    def __init__(self, color):
        super().__init__(color, Reporter.initial_positions[color], 'Reporter')


class Chief(Pawn):
    initial_positions = {
        'red': (0, 0),
        'yellow': (0, 8),
        'blue': (8, 8),
        'green': (8, 0)
    }

    def __init__(self, color):
        super().__init__(color, Chief.initial_positions[color], 'Chief')


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

    def can_move(self, new_position):
        # Check if the new position is outside the board
        if not (0 <= new_position[0] < 9 and 0 <= new_position[1] < 9):
            return False
        # Check if the new position is a valid move for the pawn
        dx = new_position[0] - self.position[0]
        dy = new_position[1] - self.position[1]
        return (dx == 0 or dy == 0 or abs(dx) == abs(dy)) and max(abs(dx), abs(dy)) <= 2


class Diplomat(Pawn):
    initial_positions = {
        'red': (0, 1),
        'yellow': (0, 7),
        'blue': (8, 7),
        'green': (8, 1)
    }

    def __init__(self, color):
        super().__init__(color, Diplomat.initial_positions[color], 'Diplomat')


class Necromobile(Pawn):
    initial_positions = {
        'red': (2, 2),
        'yellow': (2, 6),
        'blue': (6, 6),
        'green': (6, 2)
    }

    def __init__(self, color):
        super().__init__(color, Necromobile.initial_positions[color], 'Necromobile')
