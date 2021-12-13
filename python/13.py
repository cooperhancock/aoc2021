from dataclasses import dataclass

report = ''
REPORTFILE = "C:\\Users\\coope\\Documents\\aoc2021\\13.txt"
with open(REPORTFILE, 'r') as f:
    report = f.readlines()

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Fold:
    axis: str
    line: int

report = [Point(int(line.split(',')[0]), int(line.split(',')[1][:-1])) 
            if line[0] != 'f' else 
            Fold(line.split()[2][0], int(line.split()[2][2:])) 
            for line in report
         ]
print(report)
points = []
folds = []
for i in report:
    if type(i) == Point:
        points.append(i)
    else:
        folds.append(i)

print(points, folds)

def fold(pts: list[Point], fold: Fold) -> list[Point]:
    new_points = []
    for point in pts:
        if fold.axis == 'y':
            p = Point(point.x, point.y if point.y < fold.line else fold.line-(point.y-fold.line))
        else:
            p = Point(point.x if point.x < fold.line else fold.line-(point.x-fold.line), point.y)
        if not p in new_points:
            new_points.append(p)
    return new_points

points = fold(points, folds[0])
print(points)

print(f'part 1: {len(points)}')

for f in folds[1:]:
    points = fold(points, f)

print(points)

s = []
for i in range(6):
    s.append([])
    for j in range(60):
        s[i].append('.')

for p in points:
    s[p.y][p.x] = '#'

for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j], end='')
    print()
