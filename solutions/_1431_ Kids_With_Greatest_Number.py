from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    maximum = max(candies)
    return [extraCandies + item >= maximum for item in candies]
