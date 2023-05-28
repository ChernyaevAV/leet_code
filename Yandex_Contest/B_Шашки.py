"""
+++++++++++Формат ввода++++++++++++++
В первой строке даны числа
N и M (1 ≤ N, M ≤ 10^3) — размеры доски, на которой разработчики играют в шашки.
Каждое поле имеет свой цвет: черный или белый. При этом гарантируется,
что поле с координатами (1;1) имеет черный цвет.
Гарантируется также, что поле, имеющее общую границу с черным полем,
будет иметь белый цвет, а поле, имеющее общую границу с белым полем, — черный цвет.

В следующей строке дано число w — количество белых шашек на поле.
В следующих w строках задаются два целых числа (1 ≤ i ≤ N, 1 ≤ j ≤ M) — поля, на которых стоят белые шашки.
В следующей строке дано число b — количество черных шашек на поле.
В следующих b строках задаются поля с черными шашками, точно так же, как и с белыми.
Гарантируется, что количество шашек каждого цвета — целое положительное число, и что
2≤w+b≤(NM+1)/2. Гарантируется, что все шашки стоят на черных полях.
В заключительной строке ввода указано, чей ход: "white", если белых, и "black" — если черных.

++++++++++++Формат вывода+++++++++++++
В единственной строке выведите "Yes", если автор хода может срубить шашку соперника,
и "No" в противоположном случае.
  1 2 3 4 5 6 7 8
1 B W B W B W B W
2 W B W B W B W B
3 B W B W B W B W
4 W B W B W B W B
5 B W B W B W B W
6 W B W B W B W B
7 B W B W B W B W
8 W B W B W B W B

"""

from typing import Dict, List, Optional


def input_data() -> Dict:
    data: Dict[str, Optional[List, str]] = dict()
    data['board'] = list(map(int, input().split()))
    data['white'] = []
    data['black'] = []
    for _ in range(int(input())):
        data.get('white').append(list(map(int, input().split())))
    for _ in range(int(input())):
        data.get('black').append(list(map(int, input().split())))
    data['move'] = input()

    return data


def is_valid_move(coord_w, coord_b, data) -> bool:
    w_r = coord_w[0]
    w_c = coord_w[1]
    b_r = coord_b[0]
    b_c = coord_b[1]
    row = data['board'][0]
    col = data['board'][1]
    if data['move'] == 'white':
        if (
                ((w_r - b_r == -1 and w_c - b_c == -1) and
                 (1 <= w_r + 2 <= row and 1 <= w_c + 2 <= col) and
                 [w_r + 2, w_c + 2] not in data['white'] and
                 [w_r + 2, w_c + 2] not in data['black']
                ) or
                ((w_r - b_r == -1 and w_c - b_c == 1) and
                 (1 <= w_r + 2 <= row and 1 <= w_c - 2 <= col) and
                 [w_r + 2, w_c - 2] not in data['white'] and
                 [w_r + 2, w_c - 2] not in data['black']
                ) or
                ((w_r - b_r == 1 and w_c - b_c == 1) and
                 (1 <= w_r - 2 <= row and 1 <= w_c - 2 <= col) and
                 [w_r - 2, w_c - 2] not in data['white'] and
                 [w_r - 2, w_c - 2] not in data['black']
                ) or
                ((w_r - b_r == 1 and w_c - b_c == -1) and
                 (1 <= w_r - 2 <= row and 1 <= w_c + 2 <= col) and
                 [w_r - 2, w_c + 2] not in data['white'] and
                 [w_r - 2, w_c + 2] not in data['black']
                )
        ):
            return True

    elif data['move'] == 'black':
        if (
                ((b_r - w_r == -1 and b_c - w_c == -1) and
                 (1 <= b_r + 2 <= row and 1 <= b_c + 2 <= col) and
                 [b_r + 2, b_c + 2] not in data['white'] and
                 [b_r + 2, b_c + 2] not in data['black']
                ) or
                ((b_r - w_r == -1 and b_c - w_c == 1) and
                 (1 <= b_r + 2 <= row and 1 <= b_c - 2 <= row) and
                 [b_r + 2, b_c - 2] not in data['white'] and
                 [b_r + 2, b_c - 2] not in data['black']
                ) or
                ((b_r - w_r == 1 and b_c - w_c == 1) and
                 (1 <= b_r - 2 <= row and 1 <= b_c - 2 <= col) and
                 [b_r - 2, b_c - 2] not in data['white'] and
                 [b_r - 2, b_c - 2] not in data['black']
                ) or
                ((b_r - w_r == 1 and b_c - w_c == -1) and
                 (1 <= b_r - 2 <= row and 1 <= b_c + 2 <= col) and
                 [b_r - 2, b_c + 2] not in data['white'] and
                 [b_r - 2, b_c + 2] not in data['black']
                )
        ):
            return True
    return False


def search_valid_move(data: Dict) -> str:
    first_move = data.get('move')
    if first_move == 'white':
        for coord_w in data['white']:
            for coord_b in data['black']:
                if is_valid_move(coord_w, coord_b, data):
                    return 'Yes'
    elif first_move == 'black':
        for coord_b in data['black']:
            for coord_w in data['white']:
                if is_valid_move(coord_w, coord_b, data):
                    return 'Yes'
    return 'No'


def main():
    data = input_data()
    print(search_valid_move(data))


class TestCase:
    def test_white_1(self):
        data = {'board': [8, 8], 'white': [[1, 1], [2, 6], [6, 6]],
                'black': [[2, 2], [7, 7], [8, 8]], 'move': 'white'}
        answer = 'Yes'
        res = search_valid_move(data)
        assert res == answer

    def test_white_2(self):
        data = {'board': [5, 5], 'white': [[1, 1]],
                'black': [[2, 2]], 'move': 'white'}
        answer = 'Yes'
        res = search_valid_move(data)
        assert res == answer

    def test_white_3(self):
        data = {'board': [8, 8], 'white': [[1, 1]], 'black': [[2, 2]],
                'move': 'white'}
        answer = 'Yes'
        res = search_valid_move(data)
        assert res == answer

    def test_white_4(self):
        data = {'board': [8, 8], 'white': [[1, 8]], 'black': [[2, 7]],
                'move': 'white'}
        answer = 'Yes'
        res = search_valid_move(data)
        assert res == answer

    def test_white_5(self):
        data = {'board': [8, 8], 'white': [[2, 7]], 'black': [[8, 1]],
                'move': 'white'}
        answer = 'No'
        res = search_valid_move(data)
        assert res == answer

    def test_white_6(self):
        data = {'board': [8, 8], 'white': [[7, 7]], 'black': [[8, 8]],
                'move': 'white'}
        answer = 'No'
        res = search_valid_move(data)
        assert res == answer

    def test_white_7(self):
        data = {'board': [8, 8], 'white': [[2, 2]], 'black': [[3, 3]],
                'move': 'white'}
        answer = 'Yes'
        res = search_valid_move(data)
        assert res == answer

    def test_white_8(self):
        data = {'board': [8, 8], 'white': [[8, 8]], 'black': [[7, 7]],
                'move': 'white'}
        answer = 'Yes'
        res = search_valid_move(data)
        assert res == answer

    def test_white_9(self):
        data = {'board': [8, 8], 'white': [[2, 2]], 'black': [[1, 1]],
                'move': 'white'}
        answer = 'No'
        res = search_valid_move(data)
        assert res == answer

    def test_white_10(self):
        data = {'board': [8, 8], 'white': [[8, 8], [6,6]], 'black': [[7, 7]],
                'move': 'white'}
        answer = 'No'
        res = search_valid_move(data)
        assert res == answer

    def test_black_1(self):
        data = {'board': [8, 8], 'white': [[1, 1]], 'black': [[2, 2]],
                'move': 'black'}
        answer = 'No'
        res = search_valid_move(data)
        assert res == answer

    def test_black_2(self):
        data = {'board': [8, 8], 'white': [[1, 8]], 'black': [[2, 7]],
                'move': 'black'}
        answer = 'No'
        res = search_valid_move(data)
        assert res == answer

    def test_black_3(self):
        data = {'board': [8, 8], 'white': [[2, 7]], 'black': [[1, 8]],
                'move': 'black'}
        answer = 'Yes'
        res = search_valid_move(data)
        assert res == answer

    def test_black_4(self):
        data = {'board': [8, 8], 'white': [[7, 7]], 'black': [[8, 8]],
                'move': 'black'}
        answer = 'Yes'
        res = search_valid_move(data)
        assert res == answer

    def test_black_5(self):
        data = {'board': [8, 8], 'white': [[2, 2]], 'black': [[3, 3]],
                'move': 'black'}
        answer = 'Yes'
        res = search_valid_move(data)
        assert res == answer

    def test_black_6(self):
        data = {'board': [8, 8], 'white': [[8, 8]], 'black': [[7, 7]],
                'move': 'black'}
        answer = 'No'
        res = search_valid_move(data)
        assert res == answer

    def test_black_7(self):
        data = {'board': [8, 8], 'white': [[2, 2]], 'black': [[1, 1]],
                'move': 'black'}
        answer = 'Yes'
        res = search_valid_move(data)
        assert res == answer

    def test_black_8(self):
        data = {'board': [8, 8], 'white': [[8, 8], [6,6]], 'black': [[7, 7]],
                'move': 'black'}
        answer = 'Yes'
        res = search_valid_move(data)
        assert res == answer

    def test_black_9(self):
        data = {'board': [8, 8], 'white': [[3, 3], [5, 5], [7, 2], [6, 3], [6, 5]],
                'black': [[5, 4]],
                'move': 'black'}
        answer = 'Yes'
        res = search_valid_move(data)
        assert res == answer

    def test_black_10(self):
        data = {'board': [8, 8], 'white': [[2, 7], [1, 8]],
                'black': [[3, 6]],
                'move': 'black'}
        answer = 'No'
        res = search_valid_move(data)
        assert res == answer

    def test_black_11(self):
        data = {'board': [8, 8], 'white': [[2, 2], [3, 3]],
                'black': [[7, 7], [8, 8]], 'move': 'black'}
        answer = 'No'
        res = search_valid_move(data)
        assert res == answer


if __name__ == '__main__':
    main()
