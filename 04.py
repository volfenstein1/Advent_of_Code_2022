with open('input04') as file:
    data = file.read().strip().split('\n')

data = [line.replace('-', ',').split(',') for line in data]

# Part 1
total_contained = 0
for a, b, c, d in data:
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if (a <= c and d <= b) or (c <= a and b <= d):
        total_contained += 1

print('Part 1: Total contained', total_contained)


# Part 2
total_overlaps = 0
for a, b, c, d in data:
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
        total_overlaps += 1

print('Part 2: Total overlaps', total_overlaps)
