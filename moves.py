from dataclasses import dataclass
from enum import Enum
from typing import Tuple

from board import NEIGHBORS, Board, opposite_direction


class MoveKind(Enum):
    INLINE = "inline"      # 1-3 stones moving along their own line; may push opponents
    SIDESTEP = "sidestep"  # 2-3 stones moving perpendicular to their line


@dataclass(frozen=True)
class Move:
    player: int
    kind: MoveKind
    cells: Tuple[str, ...]   # 1-3 origin cells
    direction: int           # 0-5, canonical index into NEIGHBORS[cell]


def _contiguous_line(board, start, step_direction, owner, max_len):
    """Cells from `start` extending in step_direction, all owned by `owner`, capped at max_len."""
    cells = []
    cursor = start
    while cursor is not None and board[cursor] == owner and len(cells) < max_len:
        cells.append(cursor)
        cursor = NEIGHBORS[cursor][step_direction]
    return cells


def _generate_inline_moves_from(board, front, direction, player):
    """In-line moves (including sumito pushes) where `front` is the leading stone."""
    moves = []
    behind = _contiguous_line(board, front, opposite_direction(direction), player, 3)
    line = list(reversed(behind))  # back-to-front, line[-1] == front
    ahead = NEIGHBORS[front][direction]
    if ahead is None:
        return moves
    occupant = board[ahead]
    if occupant == player:
        return moves  # own stone blocks every group size equally

    for group_size in range(1, len(line) + 1):
        group = tuple(line[-group_size:])
        if occupant == '':
            moves.append(Move(player, MoveKind.INLINE, group, direction))
        else:
            opponent = 1 - player
            opp_chain = _contiguous_line(board, ahead, direction, opponent, group_size)
            if len(opp_chain) >= group_size:
                continue  # not enough of a strength advantage (1v1, 2v2, 2v3, 3v3, ...)
            beyond = NEIGHBORS[opp_chain[-1]][direction]
            if beyond is None or board[beyond] == '':
                moves.append(Move(player, MoveKind.INLINE, group, direction))
    return moves


def _generate_sidestep_moves(board, player):
    """2-3 stone side-step moves: a straight friendly line shifts perpendicular to itself
    into all-empty destination cells."""
    moves = []
    for key in NEIGHBORS:
        if board[key] != player:
            continue
        for move_dir in range(6):
            dest = NEIGHBORS[key][move_dir]
            if dest is None or board[dest] != '':
                continue
            for line_offset in (1, 2):
                axis_dir = (move_dir + line_offset) % 6
                partner1 = NEIGHBORS[key][axis_dir]
                if partner1 is None or board[partner1] != player:
                    continue
                partner1_dest = NEIGHBORS[partner1][move_dir]
                if partner1_dest is None or board[partner1_dest] != '':
                    continue
                moves.append(Move(player, MoveKind.SIDESTEP, (key, partner1), move_dir))

                partner2 = NEIGHBORS[partner1][axis_dir]
                if partner2 is None or board[partner2] != player:
                    continue
                partner2_dest = NEIGHBORS[partner2][move_dir]
                if partner2_dest is None or board[partner2_dest] != '':
                    continue
                moves.append(Move(player, MoveKind.SIDESTEP, (key, partner1, partner2), move_dir))
    return moves


def generate_legal_moves(board, player):
    moves = []
    for cell in NEIGHBORS:
        if board[cell] != player:
            continue
        for direction in range(6):
            moves.extend(_generate_inline_moves_from(board, cell, direction, player))
    moves.extend(_generate_sidestep_moves(board, player))
    return moves


def apply_move(board, move):
    """Returns a new Board with `move` applied. Never mutates `board`."""
    new_board = board.copy()
    chain = list(move.cells)

    if move.kind is MoveKind.INLINE:
        front = move.cells[-1]
        ahead = NEIGHBORS[front][move.direction]
        if ahead is not None and board[ahead] not in ('', move.player):
            opponent = 1 - move.player
            chain.extend(_contiguous_line(board, ahead, move.direction, opponent, len(move.cells)))
    # SIDESTEP: chain stays exactly move.cells - generation already guaranteed every
    # destination is empty, so there is never anything to push.

    for cell in chain:
        new_board[cell] = ''
    for cell in chain:
        dest = NEIGHBORS[cell][move.direction]
        if dest is not None:
            new_board[dest] = board[cell]  # off-board dest -> stone is captured
    return new_board
