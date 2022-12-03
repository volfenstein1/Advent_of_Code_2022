with open('input03') as file:
    data = file.read().strip().split('\n')

# Part 1
total = 0
for line in data:
    intersection = set(line[: len(line) // 2]) & set(line[len(line) // 2 :])
    for char in intersection:
        if char.islower():
            total += ord(char) - 96
        else:
            total += ord(char) - 38

print('Part 1:', total)

# Part 2
total = 0
for idx in range(0, len(data), 3):
    intersection = set(data[idx]) & set(data[idx + 1]) & set(data[idx + 2])
    for char in intersection:
        if char.islower():
            total += ord(char) - 96
        else:
            total += ord(char) - 38

print('Part 2:', total)
