a = int(input())
line = [int(e) for e in input().split()]
cnt = 0;

for x in range(0, a):
    if line[x] > 0:
        cnt += 1

print(cnt)
