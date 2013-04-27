class TicTacToeBoard:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.all_coordinates = [i + str(j) for j in [3, 2, 1]
                                for i in ['A', 'B', 'C']]
        self.status = 'Game in progress.'
        self.last_turn = ''

    def get_index(self, coordinates):
        return self.all_coordinates.index(coordinates)

    def __getitem__(self, coordinates):
        return self.board[self.get_index(coordinates)]

    def __setitem__(self, coordinates, value):
        if self.status == 'Game in progress.':
            self.check_for_invalid_turn(coordinates, value)
            self.board[self.get_index(coordinates)] = value
            self.last_turn = value
            self.check_for_winning_move(coordinates, value)
            self.check_if_board_is_full()

    def check_for_invalid_turn(self, coordinates, value):
        if coordinates not in self.all_coordinates:
            raise InvalidKey('No tile at coordinates {}'.format(coordinates))
        if self[coordinates] != ' ':
            raise InvalidMove('Tile {} is already taken'.format(coordinates))
        if value not in ['X', 'O']:
            raise InvalidValue('{} is not valid\nTry X or O'.format(value))
        if value == self.last_turn:
            raise NotYourTurn('Player {}, it is not your turn'.format(value))

    def check_for_winning_move(self, coordinates, value):
        index = self.get_index(coordinates)
        current_row = self.get_row(index // 3)
        current_column = self.get_column(index % 3)
        primary_diagonal = self.get_secondary_diagonal()
        secondary_diagonal = self.get_primary_diagonal()
        possible_winning_lines = [current_row, current_column,
                                  primary_diagonal, secondary_diagonal]
        if set(value) in [set(line) for line in possible_winning_lines]:
            self.status = "{} wins!".format(value)

    def get_row(self, row_index):
        return [self.board[i] for i in range(9) if i // 3 == row_index]

    def get_column(self, column_index):
        return [self.board[i] for i in range(9) if i % 3 == column_index]

    def get_primary_diagonal(self):
        return [self.board[i] for i in [0, 4, 8]]

    def get_secondary_diagonal(self):
        return [self.board[i] for i in [2, 4, 6]]

    def check_if_board_is_full(self):
        if ' ' not in self.board and self.status == 'Game in progress.':
            self.status = "Draw!"

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
