import random


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Player {self.name} (Color: {self.color})"

    @classmethod
    def create_players(cls):
        colors = ['RED', 'YELLOW', 'BLUE', 'GREEN']
        # Randomize the order of the colors to assign them to the players
        random.shuffle(colors)
        return [cls(color, color) for color in colors]
