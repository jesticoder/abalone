from board import Board, LOSS_THRESHOLD, render_board
from moves import apply_move
import bot
import cli

HUMAN = 'human'
COMPUTER = 'computer'


def main():
    board = Board.starting_position()
    render_board(board)

    modes = {0: COMPUTER, 1: COMPUTER}  # set either side to HUMAN to play against/watch it
    active_player = 0

    while True:
        move = (
            cli.moveselection_manual(board, active_player)
            if modes[active_player] == HUMAN
            else bot.choose_move(board, active_player)
        )
        board = apply_move(board, move)
        render_board(board)

        opponent = 1 - active_player
        if board.stones_lost(opponent) >= LOSS_THRESHOLD:
            print(f"Player {active_player} wins! Player {opponent} lost {LOSS_THRESHOLD} stones.")
            break

        active_player = opponent


if __name__ == "__main__":
    main()
