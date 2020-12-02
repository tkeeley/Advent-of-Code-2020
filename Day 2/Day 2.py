# Advent of Code Day 2

# Part 1
passwords = [line.rstrip('\n') for line in open("passwords.txt")]
x = 0

for i in range(len(passwords)):
    numbers = passwords[i].split()[0].split("-")
    char = passwords[i].split()[1].strip(":")
    pass_split = passwords[i].split()[2]
    minNum = int(numbers[0])
    maxNum = int(numbers[1])
    if pass_split.count(char) >= minNum and pass_split.count(char) <= maxNum:
        print(pass_split)
        x += 1
print("The are", x, "valid passwords")

# Part 2
passwords = [line.rstrip('\n') for line in open("passwords.txt")]
x = 0

for i in range(len(passwords)):
    numbers = passwords[i].split()[0].split("-") 
    char = passwords[i].split()[1].strip(":")
    pass_split = passwords[i].split()[2]
    firstNum = int(numbers[0]) - 1
    secondNum = int(numbers[1]) - 1
    if pass_split[firstNum] != pass_split[secondNum] and (
            pass_split[firstNum] == char or pass_split[secondNum] == char):
        x += 1

print("The are", x, "valid passwords")
