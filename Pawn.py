import constantes

class Pawn:
    def __init__(self, color, position):
        self.color = constantes.color[color.upper()]
        self.position = tuple(position)
        self.is_alive = True

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
        initial_position = Assassin.initial_positions[color]
        super().__init__(color, initial_position)
        self.type = 'Assassin'
        self.image = './assets/assassin-150x150.png'
        self.scale = (57, 57)


class Reporter(Pawn):
    initial_positions = {
        'green': (1, 1),
        'red': (1, 7),
        'blue': (7, 7),
        'yellow': (7, 1)
    }

    def __init__(self, color):
        initial_position = Reporter.initial_positions[color]
        super().__init__(color, initial_position)
        self.type = 'Reporter'
        self.image = './assets/reporter-150x150.png'
        self.scale = (57, 57)


class Chief(Pawn):
    initial_positions = {
        'green': (0, 0),
        'red': (0, 8),
        'blue': (8, 8),
        'yellow': (8, 0)
    }

    def __init__(self, color):
        initial_position = Chief.initial_positions[color]
        super().__init__(color, initial_position)
        self.type = 'Chief'
        self.image = './assets/chef-150x150.png'
        self.scale = (57, 57)


class Militant(Pawn):
    initial_positions = {
        'green': [(2, 0), (2, 1), (0, 2), (1, 2)],
        'red': [(0, 6), (1, 6), (2, 7), (2, 8)],
        'blue': [(7, 6), (8, 6), (6, 7), (6, 8)],
        'yellow': [(6, 0), (6, 1), (7, 2), (8, 2)]
    }

    def __init__(self, color, index):
        initial_position = Militant.initial_positions[color][index]
        super().__init__(color, initial_position)
        self.type = 'Militant'
        self.image = './assets/militant-150x150.png'
        self.scale = (57, 57)


class Diplomat(Pawn):
    initial_positions = {
        'green': (0, 1),
        'red': (0, 7),
        'blue': (8, 7),
        'yellow': (8, 1)
    }

    def __init__(self, color):
        initial_position = Diplomat.initial_positions[color]
        super().__init__(color, initial_position)
        self.type = 'Diplomate'
        self.image = './assets/diplomate-150x150.png'
        self.scale = (57, 57)


class Necromobile(Pawn):
    initial_positions = {
        'green': (2, 2),
        'red': (2, 6),
        'blue': (6, 6),
        'yellow': (6, 2)
    }

    def __init__(self, color):
        initial_position = Necromobile.initial_positions[color]
        super().__init__(color, initial_position)
        self.type = 'Necromobile'
        self.image = './assets/necromobile-150x150.png'
        self.scale = (57, 57)
