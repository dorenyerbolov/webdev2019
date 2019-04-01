arr = []

for x in range(0, int(input())):
    arr.append([input(), float(input())])

second = sorted(set([grade for name, grade in arr]))[1]

for name, grade in sorted(arr):
    if grade == second:
        print(name)
