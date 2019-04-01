a = int(input())
line = [int(e) for e in input().split()]

for x in range(0, a):
    if x % 2 == 0:
        print(line[x])
