def sum13(nums):
    res = 0

    for x in range(len(nums)):
        if nums[x] != 13:
            if x == 0 or nums[x - 1] != 13:
                res += nums[x]

    return res
