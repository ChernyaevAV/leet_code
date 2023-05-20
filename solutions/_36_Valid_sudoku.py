from typing import List

import pytest


def isValidSudoku(board: List[List[str]]) -> bool:
    rows = [[] for _ in range(9)]
    columns = [[] for _ in range(9)]
    blocks = [[[] for _ in range(3)] for _ in range(3)]

    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            if cell == ".":
                continue
            if (    cell in rows[i] or
                    cell in columns[j] or
                    cell in blocks[i // 3][j // 3]
            ):
                return False
            rows[i].append(cell)
            columns[j].append(cell)
            blocks[i // 3][j // 3].append(cell)
    return True

class TestCase:
    def test_true(self):
        self.board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        self.res = True
        assert isValidSudoku(self.board) == self.res

    def test_false(self):
        self.board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        self.res = False
        assert isValidSudoku(self.board) == self.res


if __name__ == '__main__':
    pytest.main()