
def load_data(n, m):
    matrix = [input() for _ in range(n)]
    return matrix


def check_list_on_5_elem(seq):
    return ('XXXXX' in seq) or ('OOOOO' in seq)


def check_frame_diagonal(matrix):
    n = len(matrix)
    m = len(matrix[0])
    if m < 5:
        return False

    diag1 = ((matrix[i][i + k] for i in range(n) if i + k < m)
                                    for k in range(m - 4))
    diag2 = ((matrix[i + k][i] for i in range(n) if i + k < n)
                                   for k in range(n - 4))
    diag3 = ((matrix[i][m - 1 - i - k]
                  for i in range(n) if m - 1 - i - k >= 0)
                  for k in range(m - 4))
    diag4 = ((matrix[i + k][m - 1 - i]
                for i in range(n) if i + k < n and m - 1 - i >= 0)
                for k in range(n - 4))

    # for diagonals in (diag1, diag2, diag3, diag4):
    #     for diag in diagonals:
    #         res = tuple(diag)
    #         print(res)

    for diagonals in (diag1, diag2, diag3, diag4):
        for diag in diagonals:
            if check_list_on_5_elem(''.join(diag)):
                return True
    return False


def check_columns(matrix):
    n = len(matrix)
    m = len(matrix[0])
    columns = (''.join([matrix[i][j] for i in range(n)]) for j in range(m))
    for col in columns:
        if check_list_on_5_elem(''.join(col)):
            return True
    return False


def check_rows(matrix):
    return any((check_list_on_5_elem(row) for row in matrix))


def main():
    n, m = map(int, input().split())
    if n < 5 and m < 5:
        print("No")
        return

    matrix = load_data(n, m)

    if any([check_rows(matrix),
            check_columns(matrix),
            check_frame_diagonal(matrix)
           ]):
        print("Yes")
        return
    else:
        print("No")


if __name__ == '__main__':
    main()
# 8 7
# .O....O
# .O...XO
# ....X..
# ...X.OO
# ..X.O.O
# X.XX..O
# .OOOOO.
# ........


# 5 5
#
#
#
#
#
