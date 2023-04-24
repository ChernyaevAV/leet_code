from typing import List


# def lastStoneWeight(stones: List[int]) -> int:
#     while len(stones) > 1:
#         stones = sorted(stones)
#         delta = stones[-1] - stones[-2]
#         stones.pop()
#         stones.pop()
#         if delta != 0:
#             stones.append(delta)
#     return stones[-1] if len(stones) == 1 else 0


def lastStoneWeight(stones: List[int]) -> int:
    while len(stones) > 1:
        stones = sorted(stones)
        x = stones.pop()
        y = stones.pop()
        if x-y != 0:
            stones.append(x-y)
    return stones[-1] if len(stones) == 1 else 0


# def lastStoneWeight(stones: List[int]) -> int:
#     while len(stones) > 1:
#         stones = sorted(stones)
#         x = stones.pop()
#         y = stones.pop()
#         if x == y:
#             continue
#         elif x < y:
#             stones.append(y - x)
#         elif y < x:
#             stones.append(x - y)
#
#     if len(stones) == 1:
#         return stones[-1]
#     else:
#         return 0



if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    assert lastStoneWeight(stones) == 1

    # stones = [1]
    # assert lastStoneWeight(stones) == 1
    #
    # stones = []
    # assert lastStoneWeight(stones) == 0