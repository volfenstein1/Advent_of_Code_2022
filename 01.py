with open('input01') as file:
    data = file.read().strip().split('\n\n')

data = [elf.split('\n') for elf in data]
data = [[int(food) for food in elf] for elf in data]

calories_consumed = [sum(elf) for elf in data]
# Part 1
print('Part 1: Max', max(calories_consumed))

# Part 2
print('Part 2: Max Top 3', sum(sorted(calories_consumed, reverse=True)[:3]))
