import functools

report = []
REPORTFILE = "..\\5.txt"
with open(REPORTFILE, 'r') as f:
    report = f.readlines()
report_len = len(report)

lines = []
points = {}
for s in report:
    line = [tuple([int(n) for n in i.split(',')]) for i in s[:-1].split(' -> ')]
    # line: [(x1, y1), (x2, y2)]
    lines.append(line)

for [(x1, y1), (x2, y2)] in lines:
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            if (x1, i) in points.keys():
                points[(x1, i)] += 1
            else:
                points[(x1, i)] = 1
        
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            if (i, y1) in points.keys():
                points[(i, y1)] += 1
            else:
                points[(i, y1)] = 1
        
    # part 2 code:
    elif x1 - x2 == y1 - y2:
        # print(f'do this {x1} {y1} {x2} {y2}')
        coords = list(zip(range(x2, x1+1), range(y2, y1+1)) if x1 > x2 else zip(range(x1, x2+1), range(y1, y2+1)))
        for i, j in coords:
            # print(f'{i} {j}')
            if (i, j) in points.keys():
                points[(i, j)] += 1
            else:
                points[(i, j)] = 1
        
    elif x1 - x2 == (y1 - y2) * -1:
        # print(f'do this {x1} {y1} {x2} {y2}')
        coords = list(zip(range(x2, x1+1), range(y2, y1-1, -1)) if x1 > x2 else zip(range(x2, x1-1, -1), range(y2, y1+1)))
        for i, j in coords:
            # print(f'{i} {j}')
            if (i, j) in points.keys():
                points[(i, j)] += 1
            else:
                points[(i, j)] = 1
        
count = 0
for key in points:
    if points[key] > 1:
        count += 1
print(f'part 1: {count}')
