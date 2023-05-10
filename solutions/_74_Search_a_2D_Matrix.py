from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    col = len(matrix[0])-1
    row = 0
    while col >= 0 and row <= len(matrix)-1:
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
           col -= 1
        else:
            row += 1
    return False

if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    assert searchMatrix(matrix, target) == True

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    assert searchMatrix(matrix, target) == False