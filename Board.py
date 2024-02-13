class Board:
    def __init__(self):
        # Initialisation du plateau de jeu
        self.board = [
            ['green chief', 'green assassin', 'green militant', '', '', '', 'yellow militant', 'yellow assassin',
             'yellow chief'],
            ['green diplomate', 'green reporter', 'green militant', '', '', '', 'yellow militant', 'yellow reporter',
             'yellow diplomate'],
            ['green militant', 'green militant', 'green necromobile', '', '', '', 'yellow necromobile',
             'yellow militant', 'yellow militant'],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', 'laby', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['red militant', 'red militant', 'red necromobile', '', '', '', 'blue necromobile', 'blue militant',
             'blue militant'],
            ['red diplomate', 'red reporter', 'red militant', '', '', '', 'blue militant', 'blue reporter',
             'blue diplomate'],
            ['red chief', 'red assassin', 'red militant', '', '', '', 'blue militant', 'blue assassin', 'blue chief']
        ]

    def display_board(self):
        # Affichage du plateau de jeu
        for row in self.board:
            print(row)




