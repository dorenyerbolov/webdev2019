a = int(input())
cnt = 0

while 2 ** cnt < a:
    cnt += 1

print(cnt)
