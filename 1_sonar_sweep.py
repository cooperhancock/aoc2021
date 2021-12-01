report = []
REPORTFILE = "1_sonar_sweep_input.txt"
with open(REPORTFILE, 'r') as f:
    report = f.readlines()

print(f'report length: {len(report)}')

sum_larger_measurements = 0

report = [int(i) for i in report]

for i in range(1, len(report)):
    if report[i] - report[i-1] > 0:
        sum_larger_measurements += 1

print(f'# measurements larger than previous: {sum_larger_measurements}')

three_measurement_sums = []
for i in range(2, len(report)):
    three_measurement_sums.append(report[i] + report[i-1] + report[i-2])

sum_larger_measurements = 0

for i in range(1, len(three_measurement_sums)):
    if three_measurement_sums[i] - three_measurement_sums[i-1] > 0:
        sum_larger_measurements += 1

print(f'# 3-window measurements larger than previous: {sum_larger_measurements}')