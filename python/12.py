report = ''
REPORTFILE = "C:\\Users\\coope\\Documents\\aoc2021\\12.txt"
with open(REPORTFILE, 'r') as f:
    report = f.readlines()
report = [line[:-1].split('-') for line in report]
print(report)

graph: dict[str, list[str]] = {}

for pair in report:
    if pair[0] in graph.keys():
        graph[pair[0]].append(pair[1])
    else:
        graph[pair[0]] = [pair[1]]
    if pair[1] in graph.keys():
        graph[pair[1]].append(pair[0])
    else:
        graph[pair[1]] = [pair[0]]

print(graph)


