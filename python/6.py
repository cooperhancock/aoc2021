report = ''
REPORTFILE = "..\\6.txt"
with open(REPORTFILE, 'r') as f:
    report = f.readlines()
report_len = len(report)
fish = report[0][:-1].split(',')
fish = [int(x) for x in fish]

def fish_count(fish, days):
    count = [0 for i in range(9)]
    for f in fish:
        count[f] += 1
    for i in range(days):
        l = len(count)
        c0 = count[0]
        for c in range(l-1):
            count[c] = count[c+1]
        count[6] += c0
        count[8] = c0
    return sum(count)

print(f'80 days: {fish_count(fish, 80)}, 256 days: {fish_count(fish, 256)}')