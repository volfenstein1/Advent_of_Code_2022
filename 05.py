with open('input05') as file:
    data = file.read().strip().split('\n\n')

data = data[1].split('\n')
data = [line.split(' ') for line in data]


# Part 1
columns = [
    'QMGCL',
    'RDLCTFHG',
    'VJFNMTWR',
    'JFDVQP',
    'NFMSLBT',
    'RNVHCDP',
    'HCT',
    'GSJVZNHP',
    'ZFHG',
]
# follow the instructions
for instruction in data:
    num_to_move, from_col, to_col = (
        int(instruction[1]),
        int(instruction[3]),
        int(instruction[5]),
    )
    while num_to_move:
        num_to_move -= 1
        columns[to_col - 1] += columns[from_col - 1][-1]
        columns[from_col - 1] = columns[from_col - 1][:-1]

res = ''
for col in columns:
    if col:
        res += col[-1]
print('Part 1: Top of columns', res)

# Part 2
columns = [
    'QMGCL',
    'RDLCTFHG',
    'VJFNMTWR',
    'JFDVQP',
    'NFMSLBT',
    'RNVHCDP',
    'HCT',
    'GSJVZNHP',
    'ZFHG',
]
# follow the instructions
for instruction in data:
    num_to_move, from_col, to_col = (
        int(instruction[1]),
        int(instruction[3]),
        int(instruction[5]),
    )
    columns[to_col - 1] += columns[from_col - 1][-num_to_move:]
    columns[from_col - 1] = columns[from_col - 1][:-num_to_move]

res = ''
for col in columns:
    if col:
        res += col[-1]
print('Part 2: Top of columns', res)
