import math
report = ''
REPORTFILE = "..\\7.txt"
with open(REPORTFILE, 'r') as f:
    report = f.readlines()
report_len = len(report)
whales = report[0].split(',')
whales = [int(x) for x in whales]
min_fuel = math.inf
min_fuel2 = math.inf
for i in range(max(whales)):
    fuel = 0
    fuel2 = 0
    for j in range(len(whales)):
        n = abs(whales[j] - i) 
        fuel += n
        fuel2 += (n * (n + 1) // 2)
    min_fuel = min(min_fuel, fuel)
    min_fuel2 = min(min_fuel2, fuel2)

print(f'min fuel {min_fuel}')
print(f'min fuel 2 {min_fuel2}')
