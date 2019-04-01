arr = []

for x in range(0, int(input())):
    arr.append([e for e in input().split()])

nm = input()

res = [float(math) + float(phys) + float(comp) for name, math, phys, comp in arr if name == nm]

print("{0:.2f}".format(res[0] / 3))
