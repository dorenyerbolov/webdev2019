arr = [int(e) for e in input().split()]


def func(x, y):
    if (x == 0 and y == 1) or (x == 1 and y == 0):
        return 1
    else:
        return 0


print(func(arr[0], arr[1]))
