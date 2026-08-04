from moves import generate_legal_moves, apply_move


def evaluate_board(board, player):
    """Placeholder heuristic. TODO(user): replace with something that actually
    reflects position strength (center control, pushed-off stones, etc)."""
    return board.stones_on_board(player)


def choose_move(board, player):
    """TODO(user): this is where your search/selection algorithm goes.

    generate_legal_moves(board, player) gives every legal Move for `player`.
    apply_move(board, move) returns a brand-new Board and never mutates `board`,
    so recursive search is safe to write directly, e.g.:

        for move in generate_legal_moves(board, player):
            child = apply_move(board, move)
            ...recurse on child, no risk of corrupting other branches...

    This placeholder just returns the first legal move so the game loop is
    runnable end-to-end while you build the real algorithm.
    """
    legal = generate_legal_moves(board, player)
    return legal[0]
