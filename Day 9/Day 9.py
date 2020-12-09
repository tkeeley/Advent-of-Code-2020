# Advent of Code 2020 Day 9

a, b, c = 25, [], [int(n) for n in open('nums.txt')]
y = lambda n, k: any(True for j in range(a) if n - k[j] in k[j + 1:])
x = next(n for i, n in enumerate(c[a:]) if not y(n, sorted(c[i:i + a])))
for n in c:
    b += [n]
    while sum(b) > x:
        b.pop(0)
    if len(b) > 1 and sum(b) == x: break

print("Part 1: " + str(x))
print("Part 2: " + str(min(b) + max(b)))
