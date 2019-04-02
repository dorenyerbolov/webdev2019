def count_hi(str):
    match = 'hi'
    cnt = 0

    for x in range(len(str) - 1):
        if str[x:x + 2] == match:
            cnt += 1

    return cnt
