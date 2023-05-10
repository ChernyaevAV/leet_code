from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    row = len(matrix)
    col = len(matrix[0])

    low = 0
    high = (row * col) - 1

    while low <= high:
        mid = (low + high) // 2

        i = mid // col
        j = mid % col

        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    assert searchMatrix(matrix, target) == True

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    assert searchMatrix(matrix, target) == False