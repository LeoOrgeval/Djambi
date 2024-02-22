import constantes


class Pawn:
    def __init__(self, color, position, pawn_type, image_path):
        self.color = constantes.color[color.upper()]
        self.position = tuple(position)
        self.is_alive = True
        self.type = pawn_type
        self.image = image_path
        self.scale = (57, 57)  # Assume all pawns have the same scale for simplicity

    def move(self, new_position):
        self.position = tuple(new_position)


class Assassin(Pawn):
    initial_positions = {
        'green': (1, 0),
        'red': (1, 8),
        'blue': (7, 8),
        'yellow': (7, 0)
    }

    def __init__(self, color):
        super().__init__(color, Assassin.initial_positions[color], 'Assassin', constantes.ASSASSIN_IMAGE)


class Reporter(Pawn):
    initial_positions = {
        'green': (1, 1),
        'red': (1, 7),
        'blue': (7, 7),
        'yellow': (7, 1)
    }

    def __init__(self, color):
        super().__init__(color, Reporter.initial_positions[color], 'Reporter', constantes.REPORTER_IMAGE)


class Chief(Pawn):
    initial_positions = {
        'green': (0, 0),
        'red': (0, 8),
        'blue': (8, 8),
        'yellow': (8, 0)
    }

    def __init__(self, color):
        super().__init__(color, Chief.initial_positions[color], 'Chief', constantes.CHIEF_IMAGE)


class Militant(Pawn):
    initial_positions = {
        'green': [(2, 0), (2, 1), (0, 2), (1, 2)],
        'red': [(0, 6), (1, 6), (2, 7), (2, 8)],
        'blue': [(7, 6), (8, 6), (6, 7), (6, 8)],
        'yellow': [(6, 0), (6, 1), (7, 2), (8, 2)]
    }

    def __init__(self, color, index):
        initial_position = Militant.initial_positions[color][index]
        super().__init__(color, initial_position, 'Militant', constantes.MILITANT_IMAGE)


class Diplomat(Pawn):
    initial_positions = {
        'green': (0, 1),
        'red': (0, 7),
        'blue': (8, 7),
        'yellow': (8, 1)
    }

    def __init__(self, color):
        super().__init__(color, Diplomat.initial_positions[color], 'Diplomat', constantes.DIPLOMAT_IMAGE)


class Necromobile(Pawn):
    initial_positions = {
        'green': (2, 2),
        'red': (2, 6),
        'blue': (6, 6),
        'yellow': (6, 2)
    }

    def __init__(self, color):
        super().__init__(color, Necromobile.initial_positions[color], 'Necromobile', constantes.NECROMOBILE_IMAGE)
