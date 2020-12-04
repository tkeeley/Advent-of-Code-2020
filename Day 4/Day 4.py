# Advent of Code Day 4
# *Use Python 3 or you'll get an error for "re.fullmatch"'

#             ____
#            /    \
#   ._.     /___/\ \
#  :(_):    |6.6| \|
#    \\     '.-.'  O
#     \\____.-"-.____
#     '----|     |--.\
#          |==[]=|  _\\_
#           \___/    /|\
#           // \\
#          //   \\
#          \\    \\
#          _\\    \\__
#         (___|    \__)

import re

# Part 1:
allPass = open("passports.txt", "r").read().split("\n\n")
passList = []
valid = 0
creds = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
info = re.compile(r'(\w+):')

for i in allPass:
    passList.append([x for x in i.split()])

for u in passList:
    check = re.findall(info, str(u))
    if all(x in check for x in creds) == True:
        valid += 1

print("Part 1: " + str(valid))

# *********************************************************

# Part 2
allPass = open("passports.txt", "r").read().split("\n\n")
passList = []
valid = 0
creds = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
x = 0

for i in allPass:
    passList.append([x for x in str(i).split()])

info = re.compile(r'(\w+):')
information = re.compile(r'(\w+):(\S+)')

for u in passList:
    check = re.findall(info, str(u))
    test = 0
    if all(x in check for x in creds) == True:
        check = re.findall(information, str(u))
        for a, b in check:
            b = re.sub(r"[\',\]]", "", b)
            if a == 'byr':
                if 1920 <= int(b) <= 2002:
                    test += 1
            elif a == 'iyr':
                if 2010 <= int(b) <= 2020:
                    test += 1
            elif a == 'eyr':
                if 2020 <= int(b) <= 2030:
                    test += 1
            elif a == 'hgt':
                if str(b).endswith("cm"):
                    if 150 <= int(b[:-2]) <= 193:
                        test += 1
                if str(b).endswith("in"):
                    if 59 <= int(b[:-2]) <= 76:
                        test += 1
            elif a == 'hcl':
                if bool(re.fullmatch(r'#[0-9a-f]{6}', b)):
                    test += 1
            elif a == 'ecl':
                if b in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    test += 1
            elif a == 'pid':
                if len(b) == 9:
                    test += 1

        if test == 7:
            valid += 1

print("Part 2: " + str(valid))