def three_sum(nums):
    n = len(nums)
    nums.sort()
    res = []

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums)) #[[-1,-1,2],[-1,0,1]]