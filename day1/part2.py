from itertools import cycle

seen = {0}
freq = 0
for line in cycle(open('input.txt').read().splitlines()):
    freq += int(line)
    if freq in seen:
        print(freq)
        break
    seen.add(freq)