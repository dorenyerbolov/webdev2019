a = int(input())
line = [int(e) for e in input().split()]
cnt = 0

for x in range(1, a - 1):
    if line[x] > line[x - 1] and line[x] > line[x + 1]:
        cnt += 1

print(cnt)
