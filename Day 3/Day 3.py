# Advent of Code 2020 Day 3

#      *
#     /.\
#    /..'\
#    /'.'\
#   /.''.'\
#   /.'.'.\
#  /'.''.'.\
#  ^^^[_]^^

import functools #for using reduce

def findTrees(x, right, down):
    return len([
        i for i in range(0, len(x), down)
        if x[i][int(i * right / down) % len(x[0])] == '#'
    ])


with open("map.txt", 'r') as file:
    x = [value.strip() for value in file.read().splitlines()]
    print('Part 1: {}'.format(findTrees(x, 3, 1)))
    print('part 2: {}'.format(
        reduce((lambda x, y: x * y), [
            findTrees(x, right, down)
            for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        ])))
    
