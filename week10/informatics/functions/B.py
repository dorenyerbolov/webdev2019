arr = [float(e) for e in input().split()]


def func(*args):
    cnt = 1
    for x in range(0, int(args[1])):
        cnt *= args[0]
    return cnt


print(func(arr[0], arr[1]))
