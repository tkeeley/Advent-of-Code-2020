# Advent of Code 2020 Day 1

f = open("num_list.txt")
x = []
for i in f:
    x.append((int)(i.strip("\n")))
f.close()

# Part 1
for a in x:
    for b in x:
        if a + b == 2020:
            ansA = (a * b)
print(ansA)

# Part 2
for c in x:
    for d in x:
        for e in x:
            if c + d + e == 2020:
                ansB = (c * d * e)
print(ansB)
