from collections import Counter

counts = list(map(dict, [Counter(Counter(f).values()) for f in open('input.txt').read().splitlines()]))
print(sum(1 for k in counts if k.get(2)) * sum(1 for k in counts if k.get(3)))