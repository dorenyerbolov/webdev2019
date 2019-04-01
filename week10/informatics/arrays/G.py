a = int(input())
line = [int(e) for e in input().split()]

for x in range(0, int(a / 2)):
    el = line[x]
    line[x] = line[a - x - 1]
    line[a - x - 1] = el

for x in range(0, a):
    print(line[x], end=" ")
