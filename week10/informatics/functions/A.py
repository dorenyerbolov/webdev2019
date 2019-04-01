arr = [int(e) for e in input().split()]


def func(*args):
    return min(args)


print(func(arr[0], arr[1], arr[2], arr[3]))
