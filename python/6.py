report = ''
REPORTFILE = "..\\6.txt"
with open(REPORTFILE, 'r') as f:
    report = f.readlines()
report_len = len(report)
fish = report[0][:-1].split(',')
print(fish)
fish = [int(x) for x in fish]
print(fish)

for i in range(80):
    l = len(fish)
    for f in range(l):
        if fish[f] == 0:
            fish.append(8)
            fish[f] = 6
            continue
        fish[f] -= 1

print(f'fish count 80 days: {len(fish)}')

fish = report[0][:-1].split(',')
fish = [int(x) for x in fish]
count = [0 for i in range(9)]
for f in fish:
    count[f] += 1

for i in range(256):
    l = len(count)
    c0 = count[0]
    for c in range(l-1):
        count[c] = count[c+1]
    count[6] += c0
    count[8] = c0
        

print(f'total fish 256 days: {sum(count)}')