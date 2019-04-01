def split_and_join(line):
    return "-".join([string for string in line.split()])


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
