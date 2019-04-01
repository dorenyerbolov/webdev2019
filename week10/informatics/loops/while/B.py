import math

a = int(input())
cnt = 2

while cnt <= a:
    if a % cnt == 0:
        print(cnt)
        break
    cnt += 1
