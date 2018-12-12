from itertools import cycle

seen = {0}
freq = 0
for line in cycle(open('input.txt').read().splitlines()):
    freq += int(line)
    print(freq) if freq in seen else seen.add(freq)