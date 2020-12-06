# Advent of Code 2020 Day 6

#       ,--.
#      ()   \
#       /    \
#     _/______\_
#    (__________)
#    (/  @  @  \)
#    (`._,()._,')
#    (  `-'`-'  )
#     \        /
#      \,,,,,,/

g = [list(x.split()) for x in open('answers.txt').read().split('\n\n')]

part1 = 0
part2 = 0

for g in g:
    v = []
    for p in g:
        v += list(p)
    t = [1 for x in set(v) if v.count(x) == len(g)]
    part1 += len(set(v))
    part2 += (sum(t))

print('Part 1: ' + str(part1))
print('Part 2: ' + str(part2))
