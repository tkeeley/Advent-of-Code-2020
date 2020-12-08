# Advent of Code Day 8

d = open("puzzle.txt").read().splitlines()
ins = list(inst.split() for inst in d)


def run(ins):
    num = len(ins)
    s = False
    a = 0
    n = 0
    x = []
    while n not in x:
        if (num == n):
            s = True
            break
        operation, offset = ins[n]
        x.append(n)
        offsetval = offset[0] == '+' and int(offset[1:]) or -int(offset[1:])

        if operation == 'acc':
            n += 1
            a += offsetval
        elif operation == 'jmp':
            n += offsetval
        else:
            n += 1

    return a, s


# Part 1
print("Part 1: " + str(run(ins)[0]))

# Part 2
j = (i for i, ins in enumerate(ins) if ins[0] == "jmp")

for d in j:
    _, offset = ins[d]
    ins[d] = ("nop", offset)
    a, s = run(ins)
    if s:
        print("Part 2: " + str(a))
        break
    ins[d] = ("jmp", offset)