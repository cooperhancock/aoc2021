report = ''
REPORTFILE = "C:\\Users\\coope\\Documents\\aoc2021\\11.txt"
with open(REPORTFILE, 'r') as f:
    report = f.readlines()
report = [[int(s) for s in line[:-1]] for line in report]
print(report)

def flash(l: list, c: tuple[int, int]) -> int:
    i, j = c
    for v in range(-1 if i>0 else 0, 2 if i<len(l)-1 else 1):
        for h in range(-1 if j>0 else 0, 2 if j<len(l[0])-1 else 1):
            l[i+v][j+h] = 0 if (v == 0 and h == 0) or l[i+v][j+h] == 0 else l[i+v][j+h] + 1
    return 1

flashes = 0
for i in range(1000):
    flashes_this_round = 0
    #has_flashed = [[False for s in line] for line in report]
    report = [list(map(lambda x: x+1, line)) for line in report]
    while True:
        these_flashes = 0
        for x in range(len(report)):
            for y in range(len(report[x])):
                if report[x][y] > 9:
                    these_flashes += flash(report, (x, y))
        flashes += these_flashes
        flashes_this_round += these_flashes
        if these_flashes == 0:
            break
    if flashes_this_round == 100:
        print(f'all flashes {i}')


print(f'part 1: {flashes}')