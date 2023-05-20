from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:

    def is_valid_row(n):
        for i in range(n):
            valid_list = []
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in valid_list:
                    return False
                valid_list.append(board[i][j])
        return True

    def is_valid_col(n):
        for i in range(n):
            valid_list = []
            for j in range(n):
                if board[j][i] == ".":
                    continue
                if board[j][i] in valid_list:
                    return False
                valid_list.append(board[j][i])
        return True

    def is_valid_board(row: int, col: int):
        valid_list = []
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if board[i][j] == ".":
                    continue
                if board[i][j] in valid_list:
                    return False
                valid_list.append(board[i][j])
        return True

    for col in [0, 3, 6]:
        for row in [0, 3, 6]:
            if not is_valid_board(col, row):
                return False

    return is_valid_row(9) and is_valid_col(9)


if __name__ == '__main__':
    board = [
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
    res = True
    assert isValidSudoku(board) == res

    board = [
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
    res = False
    assert isValidSudoku(board) == res
