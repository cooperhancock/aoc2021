report = ''
REPORTFILE = "C:\\Users\\coope\\Documents\\aoc2021\\10.txt"
with open(REPORTFILE, 'r') as f:
    report = f.readlines()
report = [line[:-1] for line in report]
opens = ['(','{','[','<']
closes = [')','}',']','>']
points = [3, 1197, 57, 25137]
points2 = [1, 3, 2, 4]

sum = 0
sums = []
for line in report:
    sum2 = 0
    sofar = []
    for bracket in line:
        if bracket in opens:
            sofar.append(bracket)
        elif closes.index(bracket) != opens.index(sofar[-1]):
            sum += points[closes.index(bracket)]
            sofar.append('fuck u')
            break
        else:
            sofar.pop()
    if sofar[-1] != 'fuck u':
        for b in reversed(sofar):
            sum2 = sum2 * 5 + points2[opens.index(b)]
        sums.append(sum2)
        
    
print(f'part 1: {sum}')
print(f'part 2: {sorted(sums)[len(sums)//2]}')