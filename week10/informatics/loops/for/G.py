import math

a = int(input())

for x in range(2, int(math.sqrt(a)) + 1):
    if a % x == 0:
        print(x)
        break
else:
    print(a)
