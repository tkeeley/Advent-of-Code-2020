# Advent of Code Day 5

#        __
#      _|==|_
#       ('')___/
#   >--(`^^')
#     (`^'^'`)
#     `======'

x = [
    int(
        e.replace('F', '0').replace('B', '1').replace('R',
                                                      '1').replace('L', '0'),
        2) for e in open("passes.txt", "rt").read().splitlines()
]
m, n = min(x), max(x)
print("Part 1: " + str(n))
print("Part 2: " + str([
    i for i in range(m + 1, n - 2) if i not in x and i - 1 in x and i + 1 in x
][0]))
