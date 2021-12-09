import DSF

report = ''
REPORTFILE = "C:\\Users\\coope\\Documents\\aoc2021\\9.txt"
with open(REPORTFILE, 'r') as f:
    report = f.readlines()

report = [[int(s) for s in line[:-1]] for line in report]

print(report)
risk = 0
for i in range(len(report)):
    for j in range(len(report[i])):
        l = report[i][j-1] if j > 0 else 10
        r = report[i][j+1] if j < len(report[i])-1 else 10
        t = report[i-1][j] if i > 0 else 10
        b = report[i+1][j] if i < len(report)-1 else 10
        if report[i][j] < l and report[i][j] < r and report[i][j] < t and report[i][j] < b:
            risk += report[i][j] + 1

print(f'part 1: {risk}')
s = []
for i in range(len(report)):
    for j in range(len(report[i])):
        s.append((i, j))
forest = DSF.dsf(set(s))
for i in range(len(report)):
    for j in range(len(report[i])):
        if report[i][j] == 9:
            continue
        l = report[i][j-1] if j > 0 else 9
        t = report[i-1][j] if i > 0 else 9
        if l == 9 and t == 9:
            forest.make_set((i, j))
        elif l == 9:
            forest.make_set((i, j))
            forest.union((i, j), (i-1, j))
        elif t == 9:
            forest.make_set((i, j))
            forest.union((i, j), (i, j-1))
        else:
            forest.make_set((i, j))
            forest.union((i, j), (i, j-1))
            forest.union((i, j), (i-1, j))

sizes = [len(s) for s in forest.set_list().values()]
print(f'part 2: {sizes.pop(sizes.index(max(sizes))) * sizes.pop(sizes.index(max(sizes))) * sizes.pop(sizes.index(max(sizes)))}')
