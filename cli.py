from board import NEIGHBORS
from moves import generate_legal_moves


def _direction_from(cell, target_cell):
    if target_cell not in NEIGHBORS.get(cell, ()):
        return None
    return NEIGHBORS[cell].index(target_cell)


def _match_move(cells, direction, legal_moves):
    wanted = frozenset(cells)
    for move in legal_moves:
        if move.direction == direction and frozenset(move.cells) == wanted:
            return move
    return None


def _parse_and_match(cells_text, direction_text, legal_moves):
    cells = tuple(cells_text.split())
    if not (1 <= len(cells) <= 3):
        return None
    if any(cell not in NEIGHBORS for cell in cells):
        return None
    direction_cell = direction_text.strip()
    direction = _direction_from(cells[0], direction_cell)
    if direction is None:
        return None
    return _match_move(cells, direction, legal_moves)


def _print_legal_moves(legal_moves):
    for move in legal_moves:
        print(f"  {' '.join(move.cells)} -> direction toward {NEIGHBORS[move.cells[0]][move.direction]} ({move.kind.value})")


def moveselection_manual(board, player):
    legal = generate_legal_moves(board, player)
    while True:
        cells_text = input("Select the stone(s) to move (1-3 cells, e.g. 'c3' or 'c3 c4', or 'list'): ")
        if cells_text.strip().lower() == 'list':
            _print_legal_moves(legal)
            continue
        direction_text = input("Select the direction (name the adjacent cell to move toward): ")
        move = _parse_and_match(cells_text, direction_text, legal)
        if move is not None:
            return move
        print("Invalid move. Please try again.")
