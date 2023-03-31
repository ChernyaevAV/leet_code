from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    counter = 0
    if len(flowerbed) == 1:
        if flowerbed[0] == 0:
            counter += 1
        return counter >= n
    for idx, value in enumerate(flowerbed):
        if (
                (idx == 0 and value != 1 and flowerbed[idx + 1] != 1) or
                (idx == len(flowerbed) - 1 and value != 1 and flowerbed[
                    idx - 1] != 1) or
                (flowerbed[idx - 1] != 1 and value != 1 and flowerbed[
                    idx + 1] != 1)
        ):
            flowerbed[idx] = 1
            counter += 1
    return counter >= n


if __name__ == '__main__':
    flowerbed = [0, 1, 0, 1, 0, 0]
    n = 1
    print(canPlaceFlowers(flowerbed, n))
