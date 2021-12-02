input = []
INPUTFILE = "..\\2.txt"
with open(INPUTFILE, 'r') as f:
    input = f.readlines()

print(f'len {len(input)}')
horizontal = 0
depth = 0

for i in input:
    if "forward" in i:
        horizontal += int(i[-2])
    elif "up" in i: 
        depth -= int(i[-2])
    elif "down" in i:
        depth += int(i[-2])

print(f'part 1: horizontal {horizontal} depth {depth} product {horizontal * depth}')

horizontal = 0
depth = 0
aim = 0

for i in input:
    if "forward" in i:
        horizontal += int(i[-2])
        depth += aim * int(i[-2])
    elif "up" in i: 
        aim -= int(i[-2])
    elif "down" in i:
        aim += int(i[-2])

print(f'part 2: horizontal {horizontal} depth {depth} product {horizontal * depth}')