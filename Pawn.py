import constantes


class Pawn:
    def __init__(self, color, position, pawn_type):
        self.color = constantes.color[color.upper()]
        self.position = tuple(position)
        self.is_alive = True
        self.type = pawn_type
        self.image = self.get_image_path(color, pawn_type, self.is_alive)
        # Scale the image to fit the square size
        self.scale = (100, 100)

    def get_image_path(self, color, pawn_type, is_alive):
        # Determine the folder to look for the image based on the pawn's state (alive or dead)
        state_folder = "Alive" if is_alive else "Died"
        status = "" if is_alive else "_died"
        return f'./assets/{state_folder}/{pawn_type}_token_{color}{status}.png'

    def set_alive(self, alive):
        self.is_alive = alive
        # Update the image path based on the new state of the pawn (alive or dead)
        self.image = self.get_image_path(self.color, self.type, self.is_alive)

    def move(self, new_position):
        self.position = tuple(new_position)


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
