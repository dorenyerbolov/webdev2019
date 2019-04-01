a = int(input())
line = [int(e) for e in input().split()]

for x in range(1, a):
    if (line[x] > 0 and line[x - 1] > 0) or (line[x] < 0 and line[x - 1] < 0):
        print("YES")
        break
else:
    print("NO")
