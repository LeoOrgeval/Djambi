from Pawn.Pawn import Pawn
import constantes
import random

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
        self.max_range = 3

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

    # def get_possible_moves(self, teams):
    #     possible_moves = []
    #     for dx in range(-2, 3):
    #         for dy in range(-2, 3):
    #             new_position = (self.position[0] + dx, self.position[1] + dy)
    #             if self.__can_move(new_position, teams):
    #                 possible_moves.append(new_position)
    #     return possible_moves
