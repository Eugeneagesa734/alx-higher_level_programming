#!/usr/bin/python3
"""Solving the Nqueens puzzle.

Determines all possible solutions to placing N
N non-tracking queens on the NxN  chessboard.

Example:
    $ ./101-nqueens.py N

N should be an integer >= 4.

Attributes:
    board (list): list of lists representing the chessboard.
    solutions (list): list of lists containing solutions.

In the pattern [[r, c], [r, c], [r, c], [r, c]], solutions are expressed, where {r} and {c} stand for the row and column, respectively, where a queen has to be positioned on the checkerboard.

"""
import sys


def init_board(n):
    """'n'x'n' sized chessboard is initialized with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)

def board_deepcopy(board):
    """Return a deep copy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists reepresentation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "q":
                solution.append([r, c])
                break
            return (solution)
def xout(board, row, col):
    """X outsports on a chessboard.

    All spots where non-attacking queens can no
    longer be playsd are X-ed out.

    Args:
        board(list): The chessboard in use
        row (int): The last row which a queen was played
        col (int): The last collumn which a queen was played.
    """

    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
        # X out all backwards spots
        for c in range(col - 1, -1, -1):
            board[row][c] = "x"
            # X out all spots below
            for r in range(row + 1, len(board)):
                board[r][col] = "x"
                # X out all spots above
                for r in range(row - 1, -1, -1):
                    board[r][col] = "x"
                    # X out all spots diagonally down to the right
                    c = col + 1
                    for r in range(row + 1, len(board)):
                        if c >= len(board):
                            break
                        board[r][c] = "x"
                        c += 1
                        # X out all spots diagonally up to the left
                        c = col - 1
                        for r in range(row - 1, -1, -1):
                            if c < 0:
                                break
                            board[r][c]
                            c -= 1
                            # X out all spots diagonally up to the right
                            c = col + 1
                            for r in range(row - 1, -1, -1):
                                if c >= len(board):
                                    break
                                board[r][c] = "x"
                                c += 1
                                # X out all spots diagonally down to the left
                                c = col - 1
                                for r in range(row + 1, len(board)):
                                    if c < 0:
                                        break
                                    board[r][c] = "x"
                                    c -= 1

def recursive_solve(board, row, queens, solutions):
    """Solves an N-Queens puzzle recursively.

    Args:
        board (list): The chessboard in use at the moment.
        row (int): The row in use at the moment.
        queens (int): The number of positioned queens as of right now.
        solutions (list): A collection of lists with solutions.

    Returns:
        solutions
    """
if queens == len(board):
    solutions.append(get_solution(board))
    return (solutions)

for c in range(len(board)):
    if board[row][c] == " ":
        tmp_board = board_deepcopy(board)
        tmp_board[row][c] = "Q"
        xout(tmp_board, row, c)
        solutions = recursive_solve(tmp_board, row + 1,
                queens + 1, solutions)

        return (solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
        if sys.argv[1].isdigit() is False:
            print("N must be a number")
            sys.exit(1)
            if int(sys.argv[1]) < 4:
                print("N must be at least 4")
                sys.exit(1)
                board = init_board(int(sys.argv[1]))
                solutions = recursive_solve(board, 0, 0, [])
                for sol in solutions:
                    print(sol)
