def count_evens(nums):
    res = 0
    for x in nums:
        if x % 2 == 0:
            res += 1

    return res