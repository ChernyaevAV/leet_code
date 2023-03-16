from math import ceil


def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    answer = []
    n = len(s)
    chars_in_section = 2 * (num_rows - 1)

    for curr_row in range(num_rows):
        index = curr_row
        while index < n:
            answer.append(s[index])

            if curr_row != 0 and curr_row != num_rows - 1:
                chars_in_between = chars_in_section - 2 * curr_row
                second_index = index + chars_in_between

                if second_index < n:
                    answer.append(s[second_index])
            index += chars_in_section

    return "".join(answer)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    num_Rows = 3
    print(convert(s, 3)) #PAHNAPLSIIGYIR

    s = "абвгдежзиклмн"
    num_Rows = 5
    print(convert(s, num_Rows))  # аибзквжлгемдн