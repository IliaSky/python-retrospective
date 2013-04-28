from itertools import chain


class TicTacToeBoard:

    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.status = 'Game in progress.'
        self.last_turn = ''

    @staticmethod
    def all_coordinates():
        return [i + str(j) for j in [3, 2, 1] for i in ['A', 'B', 'C']]

    @staticmethod
    def get_index(coordinates):
        return TicTacToeBoard.all_coordinates().index(coordinates)

    def __getitem__(self, coordinates):
        return self.board[TicTacToeBoard.get_index(coordinates)]

    def __setitem__(self, coordinates, value):
        if self.status == 'Game in progress.':
            self.check_for_invalid_turn(coordinates, value)
            self.board[TicTacToeBoard.get_index(coordinates)] = value
            self.last_turn = value
            self.update_game_status()

    def check_for_invalid_turn(self, coordinates, value):
        if coordinates not in TicTacToeBoard.all_coordinates():
            raise InvalidKey('No tile at coordinates {}'.format(coordinates))
        if self[coordinates] != ' ':
            raise InvalidMove('Tile {} is already taken'.format(coordinates))
        if value not in ['X', 'O']:
            raise InvalidValue('{} is not valid\nTry X or O'.format(value))
        if value == self.last_turn:
            raise NotYourTurn('Player {}, it is not your turn'.format(value))

    def update_game_status(self):
        self.check_for_winner()
        self.check_for_full_board()

    def check_for_winner(self):
        rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        columns = zip(*rows)
        diagonals = [[0, 4, 8], [2, 4, 6]]
        lines = [self.get_line(indexes)
                 for indexes in list(chain(rows, columns, diagonals))]
        if set(self.last_turn) in [set(line) for line in lines]:
            self.status = "{} wins!".format(self.last_turn)

    def check_for_full_board(self):
        if ' ' not in self.board and self.status == 'Game in progress.':
            self.status = "Draw!"

    def get_line(self, cell_indexes):
        return [self.board[i] for i in cell_indexes]

    def game_status(self):
        return self.status

    def __str__(self):
        lines = ['']
        for i in [3, 2, 1]:
            lines.append(str(i) + ' | {} | {} | {} |')
        lines.append('    A   B   C  \n')
        return '\n  -------------\n'.join(lines).format(*self.board)


class InvalidKey(Exception):
    pass


class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class NotYourTurn(Exception):
    pass
