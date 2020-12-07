# Advent of Code 2020 Day 7

#                      d888b         .
#    .   *           _ ?888P_
#              ,-~~-'-/_~~~\.`-~:8o.          *
#            ,'      .:8bv'      .:88.
#           /         .:88         .:8b    .     .
#   .      /          .:8P          .:8b
#        ,'          .:8P\           .:88.
#     ,='           .:88  \           __:88g_
#      -._          .:8|  |    _..-~,~    ~;'
#         ~o..__    .:8|  | _-~   ?8b_ _.-'
#           ~~  ~~--.:88  /:___...(888)
#                                   `^'      .

# Part 1
from functools import reduce

with open('bag.txt') as file:
    e = [
        line.replace(' bags', '').strip('.').replace(', ', ' ').replace(
            ' contain', '').replace('bag', '').replace('  ', ' ').strip()
        for line in file.read().splitlines()
    ]


def bagMap(entry):
    if 'no other' in entry:
        return ' '.join(entry.split(' ')[0:2]), [], []
    else:
        bags = []
        nums = []
        x = entry.split()
        for i in range(2, len(x), 3):
            bags.append(' '.join(x[i + 1:i + 3]))
            nums.append(int(x[i]))
        return ' '.join(entry.split(' ')[0:2]), bags, nums


e = list(map(bagMap, e))


def outerBag(bags, find):
    c = [b[0] for b in bags if find in b[1]]
    if not c:
        return []
    else:
        c += reduce(lambda x, y: x + outerBag(bags, y), c, [])
        return c


print("Part 1: " + str(len(set(outerBag(e, 'shiny gold')))))


# Part 2
def innerBag(bags, bag):
    a = [b for b in bags if bag == b[0]][0]
    if not a[2]:
        return 0
    else:
        return sum([i + i * innerBag(bags, b) for b, i in zip(a[1], a[2])])


print("Part 2: " + str(innerBag(e, 'shiny gold')))
