import D04.Common as Common


def run(game):
    round_list, boards = Common.setup_game(game)
    for round_value in round_list:
        for board in boards:
            board.mark(round_value)
        for board in boards:
            if board.check():
                if len(boards) == 1:
                    return board.score(round_value)
                boards.remove(board)
