import builtins

n = int(input())
line = [int(e) for e in input().split()]
print(hash(tuple(line)))
