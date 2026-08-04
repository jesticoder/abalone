# Hexagonal Abalone board: 9 rows (a-i), 61 cells total.
# NEIGHBORS[cell] is a 6-tuple, one entry per direction (0-5), holding the
# neighboring cell name or None if that direction runs off the board.
NEIGHBORS = {
    'a1': (None, None, None, 'a2', 'b2', 'b1'),
    'a2': ('a1', None, None, 'a3', 'b3', 'b2'),
    'a3': ('a2', None, None, 'a4', 'b4', 'b3'),
    'a4': ('a3', None, None, 'a5', 'b5', 'b4'),
    'a5': ('a4', None, None, None, 'b6', 'b5'),
    'b1': (None, None, 'a1', 'b2', 'c2', 'c1'),
    'b2': ('b1', 'a1', 'a2', 'b3', 'c3', 'c2'),
    'b3': ('b2', 'a2', 'a3', 'b4', 'c4', 'c3'),
    'b4': ('b3', 'a3', 'a4', 'b5', 'c5', 'c4'),
    'b5': ('b4', 'a4', 'a5', 'b6', 'c6', 'c5'),
    'b6': ('b5', 'a5', None, None, 'c7', 'c6'),
    'c1': (None, None, 'b1', 'c2', 'd2', 'd1'),
    'c2': ('c1', 'b1', 'b2', 'c3', 'd3', 'd2'),
    'c3': ('c2', 'b2', 'b3', 'c4', 'd4', 'd3'),
    'c4': ('c3', 'b3', 'b4', 'c5', 'd5', 'd4'),
    'c5': ('c4', 'b4', 'b5', 'c6', 'd6', 'd5'),
    'c6': ('c5', 'b5', 'b6', 'c7', 'd7', 'd6'),
    'c7': ('c6', 'b6', None, None, 'd8', 'd7'),
    'd1': (None, None, 'c1', 'd2', 'e2', 'e1'),
    'd2': ('d1', 'c1', 'c2', 'd3', 'e3', 'e2'),
    'd3': ('d2', 'c2', 'c3', 'd4', 'e4', 'e3'),
    'd4': ('d3', 'c3', 'c4', 'd5', 'e5', 'e4'),
    'd5': ('d4', 'c4', 'c5', 'd6', 'e6', 'e5'),
    'd6': ('d5', 'c5', 'c6', 'd7', 'e7', 'e6'),
    'd7': ('d6', 'c6', 'c7', 'd8', 'e8', 'e7'),
    'd8': ('d7', 'c7', None, None, 'e9', 'e8'),
    'e1': (None, None, 'd1', 'e2', 'f1', None),
    'e2': ('e1', 'd1', 'd2', 'e3', 'f2', 'f1'),
    'e3': ('e2', 'd2', 'd3', 'e4', 'f3', 'f2'),
    'e4': ('e3', 'd3', 'd4', 'e5', 'f4', 'f3'),
    'e5': ('e4', 'd4', 'd5', 'e6', 'f5', 'f4'),
    'e6': ('e5', 'd5', 'd6', 'e7', 'f6', 'f5'),
    'e7': ('e6', 'd6', 'd7', 'e8', 'f7', 'f6'),
    'e8': ('e7', 'd7', 'd8', 'e9', 'f8', 'f7'),
    'e9': ('e8', 'd8', None, None, None, 'f8'),
    'f1': (None, 'e1', 'e2', 'f2', 'g1', None),
    'f2': ('f1', 'e2', 'e3', 'f3', 'g2', 'g1'),
    'f3': ('f2', 'e3', 'e4', 'f4', 'g3', 'g2'),
    'f4': ('f3', 'e4', 'e5', 'f5', 'g4', 'g3'),
    'f5': ('f4', 'e5', 'e6', 'f6', 'g5', 'g4'),
    'f6': ('f5', 'e6', 'e7', 'f7', 'g6', 'g5'),
    'f7': ('f6', 'e7', 'e8', 'f8', 'g7', 'g6'),
    'f8': ('f7', 'e8', 'e9', None, None, 'g7'),
    'g1': (None, 'f1', 'f2', 'g2', 'h1', None),
    'g2': ('g1', 'f2', 'f3', 'g3', 'h2', 'h1'),
    'g3': ('g2', 'f3', 'f4', 'g4', 'h3', 'h2'),
    'g4': ('g3', 'f4', 'f5', 'g5', 'h4', 'h3'),
    'g5': ('g4', 'f5', 'f6', 'g6', 'h5', 'h4'),
    'g6': ('g5', 'f6', 'f7', 'g7', 'h6', 'h5'),
    'g7': ('g6', 'f7', 'f8', None, None, 'h6'),
    'h1': (None, 'g1', 'g2', 'h2', 'i1', None),
    'h2': ('h1', 'g2', 'g3', 'h3', 'i2', 'i1'),
    'h3': ('h2', 'g3', 'g4', 'h4', 'i3', 'i2'),
    'h4': ('h3', 'g4', 'g5', 'h5', 'i4', 'i3'),
    'h5': ('h4', 'g5', 'g6', 'h6', 'i5', 'i4'),
    'h6': ('h5', 'g6', 'g7', None, None, 'i5'),
    'i1': (None, 'h1', 'h2', 'i2', None, None),
    'i2': ('i1', 'h2', 'h3', 'i3', None, None),
    'i3': ('i2', 'h3', 'h4', 'i4', None, None),
    'i4': ('i3', 'h4', 'h5', 'i5', None, None),
    'i5': ('i4', 'h5', 'h6', None, None, None),
}

ROWS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
SIZES = [5, 6, 7, 8, 9, 8, 7, 6, 5]
MAX_SIZE = max(SIZES)

SYMBOLS = {
    '': '·',
    1: '○',
    0: '●',
}

STARTING_STONES_PER_PLAYER = 14
LOSS_THRESHOLD = 6


def opposite_direction(direction):
    return (direction + 3) % 6


class Board:
    """Mutable stone occupancy for the 61 cells. Board topology (NEIGHBORS)
    is shared, static, and never copied - only occupancy is per-instance."""

    def __init__(self, occupants=None):
        self._cells = dict(occupants) if occupants is not None else {cell: '' for cell in NEIGHBORS}

    def __getitem__(self, cell):
        return self._cells[cell]

    def __setitem__(self, cell, value):
        self._cells[cell] = value

    def cells(self):
        return self._cells.keys()

    def copy(self):
        return Board(self._cells)

    def stones_on_board(self, player):
        return sum(1 for value in self._cells.values() if value == player)

    def stones_lost(self, player):
        return STARTING_STONES_PER_PLAYER - self.stones_on_board(player)

    @classmethod
    def starting_position(cls):
        board = cls()
        for cell in NEIGHBORS:
            if cell.startswith(('a', 'b')) or cell in {'c3', 'c4', 'c5'}:
                board[cell] = 0
            if cell.startswith(('h', 'i')) or cell in {'g3', 'g4', 'g5'}:
                board[cell] = 1
        return board


def render_board(board):
    lines = []
    for letter, size in zip(ROWS, SIZES):
        indent = MAX_SIZE - size
        cells = [SYMBOLS[board[f"{letter}{i}"]] for i in range(1, size + 1)]
        lines.append(f"{letter} " + " " * indent + " ".join(cells))
    text = "\n".join(lines)
    print()
    print(text)
    print()
    print("legend:  · empty    ○ player 1    ● player 0")
    print()
    return text
