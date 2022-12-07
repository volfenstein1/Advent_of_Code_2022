with open('input06') as file:
    data = file.read().strip()

# Part 1
marker = 0

for idx in range(len(data)):
    if len(set(data[idx : idx + 4])) == 4:
        marker = idx + 4
        break

print('Part 1: Start of packet marker,', marker)

# Part 2
marker = 0

for idx in range(len(data)):
    if len(set(data[idx : idx + 14])) == 14:
        marker = idx + 14
        break

print('Part 2: Start of message marker,', marker)
