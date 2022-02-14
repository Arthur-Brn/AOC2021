import numpy as np


class BingoCard:
    def __init__(self, tab):
        self.tab = np.array(tab)
        self.marked = np.zeros((5, 5))

    def check(self):
        winning_row = np.any(np.all(self.marked == True, axis=0))
        winning_column = np.any(np.all(self.marked == True, axis=1))

        return winning_row or winning_column

    def mark(self, number):
        self.marked[self.tab == number] = True

    def score(self, number):
        return np.sum(self.tab[self.marked == False]) * number


def setup_game(data):
    boards = []
    board = []
    for row in data[2:]:
        if row.strip() == "":
            boards.append(BingoCard(board))
            board = []
        else:
            board.append([int(elem) for elem in row.split()])
    rounds = [int(elem) for elem in data[0].split(",")]
    return rounds, boards
