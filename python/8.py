report = ''
REPORTFILE = "..\\8.txt"
with open(REPORTFILE, 'r') as f:
    report = f.readlines()

report = [i.split() for i in report]
p1input = [report[i] for i in range(1, len(report), 2)]
p2input = [report[i][:-1] for i in range(0, len(report), 2)]
print(p1input)
print(p2input)

part1 = 0
for a in p1input:
    for i in a:
        if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
            part1 += 1

part2 = 0
for pattern, x in zip(p2input, p1input):
    code: list = [''] * 10 # each index will have the code for the digit of that index, e.g. code[0] = code for digit 0
    len5:list[str] = [] # list of 5 len codes
    len6:list[str] = [] # list of 6 len codes
    # first round analysis of patterns
    for s in pattern:
        if len(s) == 2:
            code[1] = s 
        elif len(s) == 4:
            code[4] = s
        elif len(s) == 3:
            code[7] = s
        elif len(s) == 7:
            code[8] = s
        elif len(s) == 5:
            len5.append(s)
        elif len(s) == 6:
            len6.append(s)
    print(f'codes so far: {code}')
    # analyze len 5 patterns
    for i in range(len(len5)):
        #print(f'check 4 vs. 2: {int(code[4][0] in len5[i]) + int(code[4][1] in len5[i]) + int(code[4][2] in len5[i]) + int(code[4][3] in len5[i])}')
        if code[1][0] in len5[i] and code[1][1] in len5[i]:
            code[3] = len5[i] # all segments of 1 in 3 but not 5 or 2
        elif (int(code[4][0] in len5[i]) + int(code[4][1] in len5[i]) + int(code[4][2] in len5[i]) + int(code[4][3] in len5[i])) == 2:
            code[2] = len5[i] # 2 shares 2 segments with 4, 3 and 5 share 3 segments
        else:
            code[5] = len5[i] # only 5 is left
    # analyze len 6 patterns
    for i in range(len(len6)):
        if not (code[1][0] in len6[i] and code[1][1] in len6[i]):
            code[6] = len6[i] # all segments of 1 in 9 and 0 but not 6
        elif code[4][0] in len6[i] and code[4][1] in len6[i] and code[4][2] in len6[i] and code[4][3] in len6[i]:
            code[9] = len6[i] # all segments of 4 in 9 but not 6 or 0
        else:
            code[0] = len6[i] # only 0 is left
    code = [''.join(sorted(s)) for s in code]
    print(f'codes done: {code}')
    number = ''
    for s in x:
        ss = ''.join(sorted(s))
        number += str(code.index(ss))
    part2 += int(number)

print(f'part1: {part1}')
print(f'part2: {part2}')