import math

a = int(input())
cnt = 1

while cnt <= int(math.sqrt(a)):
    print(cnt ** 2)
    cnt += 1
