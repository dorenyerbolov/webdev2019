def array_count9(nums):
    cnt = 0
    for x in range(len(nums)):
        if nums[x] == 9:
            cnt += 1
    return cnt
