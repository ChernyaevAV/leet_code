import sys


def main():
    nums = list(map(int, input().split()))
    res = [nums[i - 1] < nums[i] for i in range(1, len(nums))]
    print("YES") if all(res) else print("NO")


if __name__ == "__main__":
    main()
