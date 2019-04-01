import math

a = int(input())
b = int(input())

for x in range(a, b + 1):
    num = int(math.sqrt(float(x)))
    if num * num == x:
        print(x, end=" ")
