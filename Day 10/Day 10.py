# Advent of Code 2020 Day 10

# Part 1
n = {int(i) for i in open('list.txt')}
p = 0
j = [0, 0, 1]
o = []
while n:
    o.append(p)
    for v in [1, 2, 3]:
        if p + v in n:
            n.remove(p + v)
            j[v - 1] += 1
            p += v
            break
print("Part 1: " + str(j[0] * j[2]))

# Part 2
n = {int(i) for i in open('list.txt')}
n = {n: 0 for n in n}
l = p = 0
o = []
n[0] = 1

while len(n) != len(o):
    o.append(p)
    for v in [1, 2, 3]:
        if p + v in n:
            p += v
            break

for v in o:
    for j in [1, 2, 3]:
        if v + j in n:
            n[v + j] += n[v]
            l = n[v + j]

print("Part 2: " + str(l))
