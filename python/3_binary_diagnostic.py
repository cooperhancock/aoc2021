import functools

report = []
REPORTFILE = "..\\3.txt"
with open(REPORTFILE, 'r') as f:
    report = f.readlines()
report_len = len(report)
print(f'report length: {report_len}')

# clean up \n
report = [b[:-1] for b in report]

bstr_len = len(report[0])

# part 1

# calc gamma rate by most common bit in each pos
# epsilon rate least common bit
frequency_bstr = [0] * bstr_len # frequency bstr len of each bstr in report
for s in report:
    for i in range(len(s)):
        frequency_bstr[i] += int(s[i])
gamma = [0] * bstr_len
epsilon = [0] * bstr_len
for i in range(bstr_len):
    if frequency_bstr[i] > report_len // 2:
        gamma[i] = 1
    else:
        epsilon[i] = 1

# convert to decimal
convert = [2**(i-1) for i in range(bstr_len, 0, -1)]
gamma_dec = sum([a*b for a, b in zip(gamma, convert)])
epsilon_dec = sum([a*b for a, b in zip(epsilon, convert)])

print(f'gamma * epsilon : {gamma_dec * epsilon_dec}')

# part 2

def process(bstrs: list[str], bit: int, f) -> str:
    count = len(bstrs)
    if count <= 1:
        return bstrs[0]
    sum = functools.reduce(lambda x, y: int(x) + int(y), [s[bit] for s in bstrs])
    criteria_bit = 1 if f(sum, count/2) else 0
    return process(list(filter(lambda x: True if int(x[bit]) == criteria_bit else False, bstrs)), bit + 1, f)

oxygen = [int(b) for b in str(process(report, 0, lambda x, y: x >= y))]
co2 = [int(b) for b in str(process(report, 0, lambda x, y: x < y))]

oxygen_dec = sum([a*b for a, b in zip(oxygen, convert)])
co2_dec = sum([a*b for a, b in zip(co2, convert)])

print(f'part 2: {oxygen_dec * co2_dec}')