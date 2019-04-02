def lone_sum(*args):
    map = dict()
    for a in args:
        if a not in map:
            map[a] = 1
        else:
            map[a] += 1

    res = 0

    for key, value in map.items():
        if value == 1:
            res += key

    return res
