import textwrap


def wrap(string, max_width):
    res = ""
    for x in range(0, len(string), max_width):
        if x == 0:
            res += string[x:x + max_width];
        else:
            res += "\n" + string[x:x + max_width];
    return res


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
